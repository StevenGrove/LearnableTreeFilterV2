# panoptic_fpn.res50.fpn.coco.1x.nn_syncbn

## Evaluation results for sem_seg:

|  mIoU  |  fwIoU  |  mACC  |  pACC  |
|:------:|:-------:|:------:|:------:|
| 41.937 | 68.743  | 53.378 | 80.415 |

## Evaluation results for bbox:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.374
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.576
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.406
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.206
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.406
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.495
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.312
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.491
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.513
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.313
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.550
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.661
```  

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 37.401 | 57.581 | 40.595 | 20.567 | 40.575 | 49.536 |

### Per-category bbox AP:  

| category      | AP     | category     | AP     | category       | AP     |
|:--------------|:-------|:-------------|:-------|:---------------|:-------|
| person        | 52.758 | bicycle      | 27.443 | car            | 42.403 |
| motorcycle    | 39.784 | airplane     | 61.066 | bus            | 61.810 |
| train         | 57.357 | truck        | 32.188 | boat           | 24.684 |
| traffic light | 26.303 | fire hydrant | 61.186 | stop sign      | 59.593 |
| parking meter | 42.968 | bench        | 20.451 | bird           | 32.713 |
| cat           | 61.003 | dog          | 55.821 | horse          | 51.510 |
| sheep         | 48.197 | cow          | 50.772 | elephant       | 59.268 |
| bear          | 65.833 | zebra        | 63.905 | giraffe        | 62.488 |
| backpack      | 13.081 | umbrella     | 35.215 | handbag        | 10.329 |
| tie           | 28.759 | suitcase     | 31.770 | frisbee        | 63.301 |
| skis          | 18.525 | snowboard    | 27.043 | sports ball    | 44.939 |
| kite          | 40.103 | baseball bat | 22.321 | baseball glove | 32.798 |
| skateboard    | 46.408 | surfboard    | 33.343 | tennis racket  | 40.690 |
| bottle        | 36.737 | wine glass   | 33.764 | cup            | 39.957 |
| fork          | 30.108 | knife        | 13.539 | spoon          | 11.208 |
| bowl          | 38.837 | banana       | 23.355 | apple          | 17.915 |
| sandwich      | 31.480 | orange       | 30.012 | broccoli       | 20.505 |
| carrot        | 21.494 | hot dog      | 29.506 | pizza          | 48.394 |
| donut         | 41.491 | cake         | 32.915 | chair          | 24.384 |
| couch         | 37.135 | potted plant | 22.271 | bed            | 38.827 |
| dining table  | 25.934 | toilet       | 53.818 | tv             | 52.004 |
| laptop        | 56.112 | mouse        | 58.397 | remote         | 26.078 |
| keyboard      | 48.279 | cell phone   | 32.227 | microwave      | 51.053 |
| oven          | 29.355 | toaster      | 23.357 | sink           | 34.784 |
| refrigerator  | 50.334 | book         | 14.868 | clock          | 47.719 |
| vase          | 34.712 | scissors     | 22.569 | teddy bear     | 42.238 |
| hair drier    | 0.000  | toothbrush   | 14.272 |                |        |

## Evaluation results for segm:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.336
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.543
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.357
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.150
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.360
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.491
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.289
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.445
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.463
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.268
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.498
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.611
```  

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 33.614 | 54.344 | 35.666 | 14.974 | 36.047 | 49.149 |

### Per-category segm AP:  

| category      | AP     | category     | AP     | category       | AP     |
|:--------------|:-------|:-------------|:-------|:---------------|:-------|
| person        | 44.870 | bicycle      | 15.060 | car            | 38.501 |
| motorcycle    | 29.356 | airplane     | 47.427 | bus            | 60.776 |
| train         | 56.957 | truck        | 31.863 | boat           | 19.908 |
| traffic light | 25.250 | fire hydrant | 59.349 | stop sign      | 59.542 |
| parking meter | 43.072 | bench        | 14.658 | bird           | 27.234 |
| cat           | 63.490 | dog          | 53.967 | horse          | 36.100 |
| sheep         | 40.782 | cow          | 43.067 | elephant       | 54.070 |
| bear          | 64.217 | zebra        | 53.398 | giraffe        | 46.279 |
| backpack      | 12.892 | umbrella     | 43.004 | handbag        | 11.255 |
| tie           | 27.198 | suitcase     | 32.487 | frisbee        | 60.292 |
| skis          | 1.624  | snowboard    | 18.077 | sports ball    | 44.363 |
| kite          | 28.843 | baseball bat | 19.089 | baseball glove | 35.021 |
| skateboard    | 26.001 | surfboard    | 26.588 | tennis racket  | 49.662 |
| bottle        | 35.462 | wine glass   | 29.118 | cup            | 40.035 |
| fork          | 11.371 | knife        | 8.464  | spoon          | 7.874  |
| bowl          | 36.382 | banana       | 18.052 | apple          | 17.172 |
| sandwich      | 33.337 | orange       | 29.297 | broccoli       | 19.135 |
| carrot        | 18.338 | hot dog      | 20.915 | pizza          | 46.878 |
| donut         | 42.005 | cake         | 32.123 | chair          | 15.739 |
| couch         | 31.537 | potted plant | 18.975 | bed            | 30.234 |
| dining table  | 14.012 | toilet       | 54.453 | tv             | 53.913 |
| laptop        | 55.591 | mouse        | 58.494 | remote         | 24.118 |
| keyboard      | 47.173 | cell phone   | 31.474 | microwave      | 49.961 |
| oven          | 27.478 | toaster      | 23.803 | sink           | 32.403 |
| refrigerator  | 51.755 | book         | 9.371  | clock          | 47.912 |
| vase          | 34.154 | scissors     | 14.481 | teddy bear     | 39.498 |
| hair drier    | 0.000  | toothbrush   | 11.038 |                |        |

## Evaluation results for panoptic_seg:  

|        |   PQ   |   SQ   |   RQ   |  #categories  |
|:------:|:------:|:------:|:------:|:-------------:|
|  All   | 39.168 | 77.229 | 48.070 |      133      |
| Things | 45.732 | 80.972 | 55.087 |      80       |
| Stuff  | 29.260 | 71.580 | 37.477 |      53       |
