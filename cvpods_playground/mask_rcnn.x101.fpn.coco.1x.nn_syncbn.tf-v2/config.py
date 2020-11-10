import os.path as osp

from cvpods.configs.rcnn_fpn_config import RCNNFPNConfig

_config_dict = dict(
    MODEL=dict(
        WEIGHTS="detectron2://ImageNetPretrained/FAIR/X-101-32x8d.pkl",
        MASK_ON=True,
        PIXEL_STD=[57.375, 57.120, 58.395],
        RESNETS=dict(
            DEPTH=101,
            NUM_GROUPS=32,
            WIDTH_PER_GROUP=8,
            STRIDE_IN_1X1=False,
            NORM="nnSyncBN",
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
        TRAIN=("coco_2017_train",),
        TEST=("coco_2017_val",),
    ),
    SOLVER=dict(
        IMS_PER_BATCH=16,
        BASE_LR=0.02,
        STEPS=(60000, 80000),
        MAX_ITER=90000,
    ),
    INPUT=dict(
        AUG=dict(
            TRAIN_PIPELINES=[
                ("ResizeShortestEdge",
                 dict(short_edge_length=(800,), max_size=1333, sample_style="choice")),
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


class MaskRCNNConfig(RCNNFPNConfig):
    def __init__(self):
        super(MaskRCNNConfig, self).__init__()
        self._register_configuration(_config_dict)


config = MaskRCNNConfig()
