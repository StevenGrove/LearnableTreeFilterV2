import os.path as osp

from cvpods.configs.panoptic_seg_config import PanopticSegmentationConfig

_config_dict = dict(
    MODEL=dict(
        WEIGHTS="detectron2://ImageNetPretrained/MSRA/R-50.pkl",
        MASK_ON=True,
        RESNETS=dict(
            DEPTH=50,
            NORM="nnSyncBN",
            STRIDE_IN_1X1=False,
            TF_STAGES=["res3", "res4", "res5"],
            TF_NUM_GROUPS=16,
        ),
        FPN=dict(
            NORM="nnSyncBN",
        ),
        ROI_BOX_HEAD=dict(
            NAME="FastRCNNConvFCHead",
            NUM_CONV=4,
            NUM_FC=1,
            NORM="nnSyncBN",
        ),
        ROI_MASK_HEAD=dict(
            NORM="nnSyncBN",
        ),
    ),
    DATASETS=dict(
        TRAIN=("coco_2017_train_panoptic_separated",),
        TEST=("coco_2017_val_panoptic_separated",),
    ),
    SOLVER=dict(
        LR_SCHEDULER=dict(
            STEPS=(60000, 80000),
            MAX_ITER=90000,
        ),
        OPTIMIZER=dict(
            BASE_LR=0.01,
        ),
        IMS_PER_BATCH=16,
    ),
    INPUT=dict(
        AUG=dict(
            TRAIN_PIPELINES=[
                ("ResizeShortestEdge",
                 dict(short_edge_length=(800,),
                      max_size=1333, sample_style="choice")),
                ("RandomFlip", dict()),
            ],
            TEST_PIPELINES=[
                ("ResizeShortestEdge",
                 dict(short_edge_length=800, max_size=1333, sample_style="choice")),
            ],
        )
    ),
    TEST=dict(
        PRECISE_BN=dict(ENABLED=True, NUM_ITER=200),
    ),
    OUTPUT_DIR=osp.join(
        '/data/Outputs/model_logs/cvpods_playground',
        osp.split(osp.realpath(__file__))[0].split("playground/")[-1]),
)


class CustomPanopticSegmentationConfig(PanopticSegmentationConfig):
    def __init__(self):
        super(CustomPanopticSegmentationConfig, self).__init__()
        self._register_configuration(_config_dict)


config = CustomPanopticSegmentationConfig()
