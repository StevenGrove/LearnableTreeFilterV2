# mask_rcnn.res101.fpn.coco.1x.nn_syncbn.tf-v2

## Evaluation results for bbox:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.425
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.631
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.465
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.252
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.458
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.568
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.336
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.530
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.557
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.361
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.591
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.708
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |  
|:------:|:------:|:------:|:------:|:------:|:------:|  
| 42.486 | 63.133 | 46.544 | 25.189 | 45.802 | 56.779 |

### Per-category bbox AP:  

| category      | AP     | category     | AP     | category       | AP     |  
|:--------------|:-------|:-------------|:-------|:---------------|:-------|  
| person        | 55.350 | bicycle      | 32.807 | car            | 44.613 |  
| motorcycle    | 44.062 | airplane     | 63.558 | bus            | 65.419 |  
| train         | 63.735 | truck        | 35.128 | boat           | 28.965 |  
| traffic light | 27.694 | fire hydrant | 66.916 | stop sign      | 65.899 |  
| parking meter | 45.406 | bench        | 24.440 | bird           | 36.564 |  
| cat           | 69.194 | dog          | 63.616 | horse          | 59.554 |  
| sheep         | 55.995 | cow          | 57.882 | elephant       | 64.303 |  
| bear          | 66.940 | zebra        | 67.851 | giraffe        | 67.462 |  
| backpack      | 15.678 | umbrella     | 38.367 | handbag        | 14.998 |  
| tie           | 36.138 | suitcase     | 43.468 | frisbee        | 65.683 |  
| skis          | 25.008 | snowboard    | 35.077 | sports ball    | 49.415 |  
| kite          | 46.500 | baseball bat | 33.600 | baseball glove | 36.918 |  
| skateboard    | 54.083 | surfboard    | 38.156 | tennis racket  | 46.876 |  
| bottle        | 39.965 | wine glass   | 36.761 | cup            | 42.504 |  
| fork          | 37.213 | knife        | 20.085 | spoon          | 20.960 |  
| bowl          | 41.642 | banana       | 26.304 | apple          | 22.614 |  
| sandwich      | 34.564 | orange       | 32.630 | broccoli       | 22.689 |  
| carrot        | 24.156 | hot dog      | 36.392 | pizza          | 52.695 |  
| donut         | 50.948 | cake         | 37.684 | chair          | 28.613 |  
| couch         | 43.775 | potted plant | 27.717 | bed            | 44.858 |  
| dining table  | 28.209 | toilet       | 58.289 | tv             | 57.304 |  
| laptop        | 59.238 | mouse        | 63.890 | remote         | 35.246 |  
| keyboard      | 51.249 | cell phone   | 36.119 | microwave      | 54.415 |  
| oven          | 34.151 | toaster      | 31.567 | sink           | 38.641 |  
| refrigerator  | 57.423 | book         | 17.611 | clock          | 52.796 |  
| vase          | 40.658 | scissors     | 32.700 | teddy bear     | 46.840 |  
| hair drier    | 3.016  | toothbrush   | 21.461 |                |        |


## Evaluation results for segm:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.380
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.604
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.405
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.190
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.405
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.557
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.311
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.482
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.503
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.309
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.538
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.662
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |  
|:------:|:------:|:------:|:------:|:------:|:------:|  
| 38.025 | 60.362 | 40.513 | 18.988 | 40.499 | 55.701 |

### Per-category segm AP:  

| category      | AP     | category     | AP     | category       | AP     |  
|:--------------|:-------|:-------------|:-------|:---------------|:-------|  
| person        | 47.521 | bicycle      | 18.991 | car            | 40.846 |  
| motorcycle    | 32.243 | airplane     | 49.381 | bus            | 64.044 |  
| train         | 62.803 | truck        | 34.403 | boat           | 24.425 |  
| traffic light | 26.548 | fire hydrant | 62.533 | stop sign      | 66.480 |  
| parking meter | 46.677 | bench        | 17.385 | bird           | 31.209 |  
| cat           | 67.895 | dog          | 60.455 | horse          | 42.645 |  
| sheep         | 48.482 | cow          | 49.982 | elephant       | 57.583 |  
| bear          | 66.114 | zebra        | 58.663 | giraffe        | 49.930 |  
| backpack      | 15.622 | umbrella     | 44.762 | handbag        | 15.164 |  
| tie           | 33.332 | suitcase     | 44.961 | frisbee        | 64.076 |  
| skis          | 3.287  | snowboard    | 22.391 | sports ball    | 48.744 |  
| kite          | 32.913 | baseball bat | 24.542 | baseball glove | 38.448 |  
| skateboard    | 32.463 | surfboard    | 31.357 | tennis racket  | 54.951 |  
| bottle        | 38.130 | wine glass   | 32.232 | cup            | 43.057 |  
| fork          | 17.855 | knife        | 12.485 | spoon          | 14.436 |  
| bowl          | 38.474 | banana       | 21.532 | apple          | 21.856 |  
| sandwich      | 36.134 | orange       | 31.845 | broccoli       | 21.600 |  
| carrot        | 20.104 | hot dog      | 25.272 | pizza          | 50.643 |  
| donut         | 50.933 | cake         | 37.663 | chair          | 19.098 |  
| couch         | 36.425 | potted plant | 23.244 | bed            | 34.328 |  
| dining table  | 16.076 | toilet       | 58.034 | tv             | 59.738 |  
| laptop        | 59.024 | mouse        | 63.458 | remote         | 32.165 |  
| keyboard      | 50.047 | cell phone   | 34.330 | microwave      | 56.637 |  
| oven          | 30.702 | toaster      | 34.269 | sink           | 35.775 |  
| refrigerator  | 59.158 | book         | 11.479 | clock          | 52.941 |  
| vase          | 40.002 | scissors     | 23.615 | teddy bear     | 45.021 |  
| hair drier    | 2.243  | toothbrush   | 15.658 |                |        |
