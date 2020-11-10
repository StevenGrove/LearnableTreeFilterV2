# mask_rcnn.res50.fpn.coco.1x.nn_syncbn.tf-v2

## Evaluation results for bbox:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.413
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.618
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.449
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.250
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.443
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.551
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.329
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.521
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.548
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.357
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.583
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.693
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |  
|:------:|:------:|:------:|:------:|:------:|:------:|  
| 41.278 | 61.811 | 44.923 | 25.042 | 44.319 | 55.056 |

### Per-category bbox AP:  

| category      | AP     | category     | AP     | category       | AP     |  
|:--------------|:-------|:-------------|:-------|:---------------|:-------|  
| person        | 54.540 | bicycle      | 29.913 | car            | 43.374 |  
| motorcycle    | 42.178 | airplane     | 65.174 | bus            | 63.856 |  
| train         | 64.388 | truck        | 34.277 | boat           | 27.421 |  
| traffic light | 27.880 | fire hydrant | 65.070 | stop sign      | 63.081 |  
| parking meter | 42.240 | bench        | 24.325 | bird           | 35.838 |  
| cat           | 66.241 | dog          | 61.150 | horse          | 57.743 |  
| sheep         | 52.720 | cow          | 54.688 | elephant       | 62.201 |  
| bear          | 71.023 | zebra        | 64.249 | giraffe        | 65.984 |  
| backpack      | 14.589 | umbrella     | 38.604 | handbag        | 14.801 |  
| tie           | 32.721 | suitcase     | 42.013 | frisbee        | 64.742 |  
| skis          | 21.376 | snowboard    | 36.803 | sports ball    | 49.292 |  
| kite          | 44.536 | baseball bat | 31.480 | baseball glove | 36.105 |  
| skateboard    | 52.031 | surfboard    | 38.345 | tennis racket  | 47.710 |  
| bottle        | 38.502 | wine glass   | 34.498 | cup            | 41.629 |  
| fork          | 33.552 | knife        | 18.582 | spoon          | 16.145 |  
| bowl          | 40.236 | banana       | 23.061 | apple          | 21.038 |  
| sandwich      | 33.769 | orange       | 30.333 | broccoli       | 23.442 |  
| carrot        | 23.659 | hot dog      | 30.757 | pizza          | 53.466 |  
| donut         | 49.831 | cake         | 36.329 | chair          | 27.157 |  
| couch         | 40.760 | potted plant | 26.205 | bed            | 40.879 |  
| dining table  | 27.601 | toilet       | 61.345 | tv             | 55.089 |  
| laptop        | 58.653 | mouse        | 63.257 | remote         | 30.680 |  
| keyboard      | 49.485 | cell phone   | 35.890 | microwave      | 55.040 |  
| oven          | 32.552 | toaster      | 45.224 | sink           | 36.057 |  
| refrigerator  | 54.781 | book         | 15.982 | clock          | 50.087 |  
| vase          | 38.847 | scissors     | 29.265 | teddy bear     | 45.252 |  
| hair drier    | 3.960  | toothbrush   | 24.638 |                |        |


## Evaluation results for segm:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.370
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.586
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.396
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.189
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.394
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.540
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.305
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.473
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.495
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.308
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.527
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.644
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |  
|:------:|:------:|:------:|:------:|:------:|:------:|  
| 37.048 | 58.637 | 39.642 | 18.925 | 39.352 | 53.954 |

### Per-category segm AP:  

| category      | AP     | category     | AP     | category       | AP     |  
|:--------------|:-------|:-------------|:-------|:---------------|:-------|  
| person        | 46.825 | bicycle      | 17.531 | car            | 39.708 |  
| motorcycle    | 31.827 | airplane     | 50.246 | bus            | 62.652 |  
| train         | 61.674 | truck        | 33.115 | boat           | 22.654 |  
| traffic light | 27.004 | fire hydrant | 60.687 | stop sign      | 63.747 |  
| parking meter | 43.804 | bench        | 17.705 | bird           | 29.433 |  
| cat           | 67.715 | dog          | 57.199 | horse          | 40.438 |  
| sheep         | 45.951 | cow          | 46.217 | elephant       | 57.055 |  
| bear          | 69.777 | zebra        | 54.758 | giraffe        | 50.052 |  
| backpack      | 14.100 | umbrella     | 44.809 | handbag        | 14.405 |  
| tie           | 31.290 | suitcase     | 42.275 | frisbee        | 63.316 |  
| skis          | 2.316  | snowboard    | 23.894 | sports ball    | 49.046 |  
| kite          | 32.387 | baseball bat | 24.903 | baseball glove | 38.198 |  
| skateboard    | 29.194 | surfboard    | 32.378 | tennis racket  | 53.270 |  
| bottle        | 37.223 | wine glass   | 30.610 | cup            | 42.358 |  
| fork          | 14.581 | knife        | 11.431 | spoon          | 11.768 |  
| bowl          | 37.578 | banana       | 18.149 | apple          | 20.552 |  
| sandwich      | 34.370 | orange       | 30.108 | broccoli       | 21.986 |  
| carrot        | 20.270 | hot dog      | 23.003 | pizza          | 51.431 |  
| donut         | 49.633 | cake         | 35.759 | chair          | 18.236 |  
| couch         | 33.668 | potted plant | 21.579 | bed            | 33.398 |  
| dining table  | 15.533 | toilet       | 59.550 | tv             | 56.295 |  
| laptop        | 59.277 | mouse        | 62.988 | remote         | 28.416 |  
| keyboard      | 48.003 | cell phone   | 34.695 | microwave      | 56.747 |  
| oven          | 30.851 | toaster      | 48.254 | sink           | 33.783 |  
| refrigerator  | 58.346 | book         | 10.137 | clock          | 49.740 |  
| vase          | 36.927 | scissors     | 21.989 | teddy bear     | 43.068 |  
| hair drier    | 1.337  | toothbrush   | 16.684 |                |        |
