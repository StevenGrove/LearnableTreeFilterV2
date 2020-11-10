# cascade.x101.fpn.coco.1x.nn_syncbn.tf-v2  

## Evaluation results for bbox:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.469
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.650
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.507
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.283
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.503
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.615
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.360
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.560
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.585
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.380
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.623
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.732
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |  
|:------:|:------:|:------:|:------:|:------:|:------:|  
| 46.851 | 64.993 | 50.719 | 28.262 | 50.264 | 61.497 |

### Per-category bbox AP:  

| category      | AP     | category     | AP     | category       | AP     |  
|:--------------|:-------|:-------------|:-------|:---------------|:-------|  
| person        | 59.692 | bicycle      | 35.269 | car            | 49.104 |  
| motorcycle    | 48.671 | airplane     | 70.724 | bus            | 69.041 |  
| train         | 69.282 | truck        | 39.812 | boat           | 31.077 |  
| traffic light | 30.063 | fire hydrant | 74.311 | stop sign      | 67.717 |  
| parking meter | 52.078 | bench        | 28.282 | bird           | 43.383 |  
| cat           | 74.910 | dog          | 68.356 | horse          | 64.662 |  
| sheep         | 59.844 | cow          | 63.648 | elephant       | 69.316 |  
| bear          | 73.538 | zebra        | 70.796 | giraffe        | 73.238 |  
| backpack      | 18.188 | umbrella     | 43.737 | handbag        | 19.863 |  
| tie           | 40.901 | suitcase     | 47.287 | frisbee        | 71.921 |  
| skis          | 28.111 | snowboard    | 42.818 | sports ball    | 51.822 |  
| kite          | 49.059 | baseball bat | 36.064 | baseball glove | 42.226 |  
| skateboard    | 59.970 | surfboard    | 43.862 | tennis racket  | 54.181 |  
| bottle        | 43.873 | wine glass   | 41.119 | cup            | 48.340 |  
| fork          | 44.349 | knife        | 26.866 | spoon          | 25.098 |  
| bowl          | 45.441 | banana       | 26.790 | apple          | 25.421 |  
| sandwich      | 39.058 | orange       | 32.063 | broccoli       | 25.022 |  
| carrot        | 26.717 | hot dog      | 38.864 | pizza          | 58.956 |  
| donut         | 55.546 | cake         | 40.602 | chair          | 32.762 |  
| couch         | 46.084 | potted plant | 30.881 | bed            | 48.359 |  
| dining table  | 31.659 | toilet       | 66.258 | tv             | 59.917 |  
| laptop        | 65.656 | mouse        | 64.077 | remote         | 40.372 |  
| keyboard      | 56.249 | cell phone   | 42.901 | microwave      | 59.763 |  
| oven          | 36.734 | toaster      | 40.880 | sink           | 41.129 |  
| refrigerator  | 65.921 | book         | 19.563 | clock          | 54.324 |  
| vase          | 40.313 | scissors     | 33.024 | teddy bear     | 50.663 |  
| hair drier    | 6.218  | toothbrush   | 33.408 |                |        |


## Evaluation results for segm:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.403
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.623
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.437
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.210
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.430
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.577
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.320
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.488
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.508
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.314
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.542
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.656
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |  
|:------:|:------:|:------:|:------:|:------:|:------:|  
| 40.321 | 62.320 | 43.688 | 21.035 | 43.026 | 57.671 |

### Per-category segm AP:  

| category      | AP     | category     | AP     | category       | AP     |  
|:--------------|:-------|:-------------|:-------|:---------------|:-------|  
| person        | 49.442 | bicycle      | 20.180 | car            | 43.761 |  
| motorcycle    | 37.017 | airplane     | 52.469 | bus            | 66.049 |  
| train         | 64.368 | truck        | 38.066 | boat           | 26.337 |  
| traffic light | 28.739 | fire hydrant | 68.830 | stop sign      | 65.786 |  
| parking meter | 49.172 | bench        | 19.625 | bird           | 34.097 |  
| cat           | 68.851 | dog          | 61.880 | horse          | 45.049 |  
| sheep         | 50.852 | cow          | 52.520 | elephant       | 60.438 |  
| bear          | 70.937 | zebra        | 58.110 | giraffe        | 53.918 |  
| backpack      | 18.230 | umbrella     | 46.293 | handbag        | 17.837 |  
| tie           | 35.573 | suitcase     | 47.389 | frisbee        | 67.480 |  
| skis          | 4.649  | snowboard    | 26.403 | sports ball    | 49.845 |  
| kite          | 34.733 | baseball bat | 25.214 | baseball glove | 42.689 |  
| skateboard    | 35.498 | surfboard    | 35.355 | tennis racket  | 56.893 |  
| bottle        | 40.838 | wine glass   | 35.536 | cup            | 46.388 |  
| fork          | 21.071 | knife        | 17.773 | spoon          | 15.064 |  
| bowl          | 40.284 | banana       | 20.529 | apple          | 23.630 |  
| sandwich      | 39.255 | orange       | 30.444 | broccoli       | 23.135 |  
| carrot        | 22.137 | hot dog      | 29.981 | pizza          | 54.345 |  
| donut         | 53.158 | cake         | 39.406 | chair          | 22.094 |  
| couch         | 37.565 | potted plant | 24.769 | bed            | 36.521 |  
| dining table  | 17.288 | toilet       | 60.839 | tv             | 60.581 |  
| laptop        | 62.084 | mouse        | 62.438 | remote         | 34.998 |  
| keyboard      | 52.399 | cell phone   | 38.408 | microwave      | 60.530 |  
| oven          | 33.052 | toaster      | 41.782 | sink           | 36.986 |  
| refrigerator  | 63.604 | book         | 13.836 | clock          | 53.413 |  
| vase          | 38.875 | scissors     | 21.403 | teddy bear     | 46.753 |  
| hair drier    | 0.972  | toothbrush   | 20.977 |                |        |
