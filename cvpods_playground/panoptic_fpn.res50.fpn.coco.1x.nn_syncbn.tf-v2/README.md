# panoptic_fpn.res50.fpn.coco.1x.nn_syncbn.tf-v2

## Evaluation results for sem_seg:

|  mIoU  |  fwIoU  |  mACC  |  pACC  |
|:------:|:-------:|:------:|:------:|
| 44.418 | 70.247  | 56.624 | 81.517 |

## Evaluation results for bbox:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.393
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.605
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.427
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.228
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.424
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.529
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.319
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.502
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.530
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.340
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.564
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.674
```  

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 39.336 | 60.514 | 42.651 | 22.758 | 42.405 | 52.876 |

### Per-category bbox AP:  

| category      | AP     | category     | AP     | category       | AP     |
|:--------------|:-------|:-------------|:-------|:---------------|:-------|
| person        | 52.868 | bicycle      | 28.526 | car            | 42.406 |
| motorcycle    | 42.517 | airplane     | 64.651 | bus            | 62.983 |
| train         | 62.027 | truck        | 33.293 | boat           | 26.113 |
| traffic light | 27.905 | fire hydrant | 63.170 | stop sign      | 59.105 |
| parking meter | 41.815 | bench        | 23.386 | bird           | 35.038 |
| cat           | 65.296 | dog          | 58.245 | horse          | 55.122 |
| sheep         | 50.782 | cow          | 55.740 | elephant       | 60.605 |
| bear          | 66.193 | zebra        | 64.801 | giraffe        | 61.831 |
| backpack      | 12.398 | umbrella     | 37.101 | handbag        | 11.249 |
| tie           | 29.682 | suitcase     | 38.630 | frisbee        | 62.336 |
| skis          | 21.315 | snowboard    | 29.995 | sports ball    | 48.059 |
| kite          | 42.345 | baseball bat | 25.649 | baseball glove | 34.910 |
| skateboard    | 49.150 | surfboard    | 34.718 | tennis racket  | 41.616 |
| bottle        | 37.424 | wine glass   | 33.206 | cup            | 39.110 |
| fork          | 30.065 | knife        | 15.384 | spoon          | 12.600 |
| bowl          | 40.490 | banana       | 23.354 | apple          | 19.066 |
| sandwich      | 31.275 | orange       | 30.343 | broccoli       | 22.107 |
| carrot        | 24.111 | hot dog      | 32.616 | pizza          | 50.254 |
| donut         | 46.247 | cake         | 36.865 | chair          | 26.698 |
| couch         | 39.305 | potted plant | 26.142 | bed            | 42.817 |
| dining table  | 27.866 | toilet       | 58.408 | tv             | 55.315 |
| laptop        | 56.877 | mouse        | 61.769 | remote         | 28.192 |
| keyboard      | 49.426 | cell phone   | 33.950 | microwave      | 52.072 |
| oven          | 30.551 | toaster      | 27.248 | sink           | 37.451 |
| refrigerator  | 52.133 | book         | 14.189 | clock          | 50.865 |
| vase          | 37.355 | scissors     | 26.461 | teddy bear     | 42.056 |
| hair drier    | 0.000  | toothbrush   | 21.646 |                |        |

## Evaluation results for segm:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.354
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.570
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.378
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.171
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.375
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.526
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.299
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.457
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.479
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.293
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.509
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.631
```  

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 35.439 | 56.999 | 37.769 | 17.111 | 37.486 | 52.600 |

### Per-category segm AP:  

| category      | AP     | category     | AP     | category       | AP     |
|:--------------|:-------|:-------------|:-------|:---------------|:-------|
| person        | 45.188 | bicycle      | 16.251 | car            | 38.451 |
| motorcycle    | 31.094 | airplane     | 49.309 | bus            | 62.331 |
| train         | 60.405 | truck        | 32.461 | boat           | 22.340 |
| traffic light | 26.763 | fire hydrant | 59.721 | stop sign      | 58.990 |
| parking meter | 42.599 | bench        | 16.371 | bird           | 29.985 |
| cat           | 65.873 | dog          | 55.629 | horse          | 39.729 |
| sheep         | 44.823 | cow          | 46.965 | elephant       | 55.131 |
| bear          | 64.591 | zebra        | 53.623 | giraffe        | 46.178 |
| backpack      | 12.461 | umbrella     | 44.604 | handbag        | 12.066 |
| tie           | 29.025 | suitcase     | 41.386 | frisbee        | 60.463 |
| skis          | 2.135  | snowboard    | 19.620 | sports ball    | 47.635 |
| kite          | 29.777 | baseball bat | 21.636 | baseball glove | 37.048 |
| skateboard    | 27.506 | surfboard    | 27.815 | tennis racket  | 50.075 |
| bottle        | 35.759 | wine glass   | 28.656 | cup            | 39.557 |
| fork          | 11.906 | knife        | 9.106  | spoon          | 8.399  |
| bowl          | 38.403 | banana       | 17.586 | apple          | 18.714 |
| sandwich      | 32.939 | orange       | 29.698 | broccoli       | 20.984 |
| carrot        | 20.926 | hot dog      | 22.958 | pizza          | 49.192 |
| donut         | 46.556 | cake         | 36.938 | chair          | 17.033 |
| couch         | 33.427 | potted plant | 22.045 | bed            | 35.410 |
| dining table  | 14.993 | toilet       | 57.348 | tv             | 56.642 |
| laptop        | 56.952 | mouse        | 61.291 | remote         | 26.165 |
| keyboard      | 48.663 | cell phone   | 33.544 | microwave      | 53.696 |
| oven          | 30.258 | toaster      | 30.488 | sink           | 34.754 |
| refrigerator  | 52.931 | book         | 9.557  | clock          | 50.746 |
| vase          | 36.808 | scissors     | 18.899 | teddy bear     | 41.640 |
| hair drier    | 0.990  | toothbrush   | 14.527 |                |        |

## Evaluation results for panoptic_seg:  

|        |   PQ   |   SQ   |   RQ   |  #categories  |
|:------:|:------:|:------:|:------:|:-------------:|
|  All   | 41.713 | 78.834 | 50.878 |      133      |
| Things | 47.555 | 80.956 | 57.270 |      80       |
| Stuff  | 32.894 | 75.629 | 41.228 |      53       |
