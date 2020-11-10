# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
"""
Testing Script for cvpods.

This scripts reads a given config file and runs the training or evaluation.
It is an entry point that is made to train standard models in cvpods.

In order to let one script support training of many models,
this script contains logic that are specific to these built-in models and therefore
may not be suitable for your own project.
For example, your research project perhaps only needs a single "evaluator".

Therefore, we recommend you to use cvpods as an library and take
this file as an example of how to use the library.
You may want to write your own script with your datasets and other customizations.
"""
import glob
import logging
import os
import re
import sys
from collections import OrderedDict

from torch.nn.parallel import DistributedDataParallel

from cvpods.checkpoint import DetectionCheckpointer
from cvpods.engine import DefaultTrainer, default_argument_parser, default_setup, launch
from cvpods.evaluation import build_evaluator, verify_results
from cvpods.modeling import GeneralizedRCNNWithTTA, GeneralizedRCNN, TTAWarper
from cvpods.utils import PathManager, comm

sys.path.insert(0, '.')
from config import config  # noqa: E402
from net import build_model  # noqa: E402


class Trainer(DefaultTrainer):
    """
    We use the "DefaultTrainer" which contains a number pre-defined logic for
    standard training workflow. They may not work for you, especially if you
    are working on a new research project. In that case you can use the cleaner
    "SimpleTrainer", or write your own training loop.
    """

    @classmethod
    def build_evaluator(cls, cfg, dataset_name, dataset, output_folder=None):
        """
        Create evaluator(s) for a given dataset.
        This uses the special metadata "evaluator_type" associated with each builtin dataset.
        For your own dataset, you can simply create an evaluator manually in your
        script and do not have to worry about the hacky if-else logic here.
        """
        dump_test = config.GLOBAL.DUMP_TEST
        return build_evaluator(cfg, dataset_name, dataset, output_folder, dump=dump_test)

    @classmethod
    def test_with_TTA(cls, cfg, model):
        logger = logging.getLogger("cvpods.trainer")
        # In the end of training, run an evaluation with TTA
        # Only support some R-CNN models.
        logger.info("Running inference with test-time augmentation ...")

        module = model
        if isinstance(module, DistributedDataParallel):
            module = model.module
        if isinstance(module, GeneralizedRCNN):
            model = GeneralizedRCNNWithTTA(cfg, model)
        else:
            model = TTAWarper(cfg, model)
        res = cls.test(cfg, model, output_folder=os.path.join(cfg.OUTPUT_DIR, "inference_TTA"))
        res = OrderedDict({k + "_TTA": v for k, v in res.items()})
        return res


def test_argument_parser():
    parser = default_argument_parser()
    parser.add_argument("--start-iter", type=int, default=0, help="start iter used to test")
    parser.add_argument("--end-iter", type=int, default=None,
                        help="end iter used to test")
    parser.add_argument("--debug", action="store_true", help="use debug mode or not")
    return parser


def main(args):
    config.merge_from_list(args.opts)
    cfg, logger = default_setup(config, args)
    if args.debug:
        batches = int(cfg.SOLVER.IMS_PER_BATCH / 8 * args.num_gpus)
        if cfg.SOLVER.IMS_PER_BATCH != batches:
            cfg.SOLVER.IMS_PER_BATCH = batches
            logger.warning("SOLVER.IMS_PER_BATCH is changed to {}".format(batches))

    if "MODEL.WEIGHTS" in args.opts:
        if cfg.MODEL.WEIGHTS.endswith(".pth") and not PathManager.exists(cfg.MODEL.WEIGHTS):
            ckpt_name = cfg.MODEL.WEIGHTS.split("/")[-1]
            model_prefix = cfg.OUTPUT_DIR.split("cvpods_playground")[1][1:]
            remote_file_path = os.path.join(cfg.OSS.DUMP_PREFIX, model_prefix, ckpt_name)
            logger.warning(f"The specified ckpt file ({cfg.MODEL.WEIGHTS}) was not found locally,"
                           f" try to load the corresponding dump file on OSS ({remote_file_path}).")
            cfg.MODEL.WEIGHTS = remote_file_path
        valid_files = [cfg.MODEL.WEIGHTS]
    else:
        list_of_files = glob.glob(os.path.join(cfg.OUTPUT_DIR, '*.pth'))
        if len(list_of_files) == 0:
            oss_prefix = os.path.join(cfg.OSS.MODEL_PREFIX, "model_zoo")
            model_prefix = '/'.join(os.getcwd().split('/')[-5:])
            file_path = os.path.join(oss_prefix, model_prefix, "model_final.pth")
            logger.warning(f"No checkpoint file found in the local log path ({cfg.OUTPUT_DIR}), "
                           f"trying to get it from Model Zoo (OSS URI: {file_path}).")
            assert PathManager.isfile(file_path), f"No checkpoint file found in {file_path}."
            valid_files = [file_path]
        else:
            assert list_of_files, "No checkpoint file found in {}.".format(cfg.OUTPUT_DIR)
            list_of_files.sort(key=os.path.getctime)
            latest_file = list_of_files[-1]
            if not args.end_iter:
                valid_files = [latest_file]
            else:
                files = [f for f in list_of_files if str(f) <= str(latest_file)]
                valid_files = []
                for f in files:
                    try:
                        model_iter = int(re.split(r'(model_|\.pth)', f)[-3])
                    except Exception:
                        logger.warning("remove {}".format(f))
                        continue
                    if args.start_iter <= model_iter <= args.end_iter:
                        valid_files.append(f)
                assert valid_files, "No .pth files satisfy your requirement"

    # * means all if need specific format then *.csv
    for current_file in valid_files:
        cfg.MODEL.WEIGHTS = current_file
        model = build_model(cfg)

        DetectionCheckpointer(model, save_dir=cfg.OUTPUT_DIR).resume_or_load(
            cfg.MODEL.WEIGHTS, resume=args.resume
        )
        if cfg.TEST.AUG.ENABLED:
            res = Trainer.test_with_TTA(cfg, model)
        else:
            res = Trainer.test(cfg, model)

        if comm.is_main_process():
            verify_results(cfg, res)

    # return res


if __name__ == "__main__":
    args = test_argument_parser().parse_args()
    print("Command Line Args:", args)
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )
