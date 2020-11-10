# mask_rcnn.x101.fpn.coco.1x.nn_syncbn.tf-v2

## Evaluation results for bbox:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.445
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.653
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.488
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.273
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.480
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.582
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.345
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.540
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.565
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.375
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.606
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.705
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 44.499 | 65.271 | 48.755 | 27.266 | 48.020 | 58.161 |

### Per-category bbox AP:  

| category      | AP     | category     | AP     | category       | AP     |
|:--------------|:-------|:-------------|:-------|:---------------|:-------|
| person        | 56.519 | bicycle      | 35.038 | car            | 45.733 |
| motorcycle    | 45.510 | airplane     | 66.075 | bus            | 67.219 |
| train         | 67.067 | truck        | 38.310 | boat           | 28.207 |
| traffic light | 30.033 | fire hydrant | 70.850 | stop sign      | 65.356 |
| parking meter | 47.424 | bench        | 27.474 | bird           | 40.450 |
| cat           | 69.782 | dog          | 64.321 | horse          | 61.996 |
| sheep         | 55.806 | cow          | 59.692 | elephant       | 66.308 |
| bear          | 72.317 | zebra        | 67.053 | giraffe        | 68.776 |
| backpack      | 18.544 | umbrella     | 41.181 | handbag        | 18.908 |
| tie           | 37.261 | suitcase     | 43.912 | frisbee        | 66.154 |
| skis          | 27.150 | snowboard    | 43.378 | sports ball    | 48.836 |
| kite          | 46.242 | baseball bat | 35.416 | baseball glove | 39.087 |
| skateboard    | 55.465 | surfboard    | 41.506 | tennis racket  | 51.599 |
| bottle        | 41.210 | wine glass   | 39.524 | cup            | 45.291 |
| fork          | 41.611 | knife        | 25.162 | spoon          | 23.336 |
| bowl          | 43.174 | banana       | 27.284 | apple          | 23.591 |
| sandwich      | 38.746 | orange       | 32.313 | broccoli       | 23.607 |
| carrot        | 25.156 | hot dog      | 33.093 | pizza          | 53.834 |
| donut         | 52.537 | cake         | 40.961 | chair          | 31.485 |
| couch         | 44.746 | potted plant | 30.062 | bed            | 44.502 |
| dining table  | 29.979 | toilet       | 63.614 | tv             | 58.387 |
| laptop        | 62.351 | mouse        | 60.275 | remote         | 39.872 |
| keyboard      | 54.259 | cell phone   | 40.685 | microwave      | 57.689 |
| oven          | 39.065 | toaster      | 29.299 | sink           | 37.999 |
| refrigerator  | 62.280 | book         | 17.675 | clock          | 53.344 |
| vase          | 41.061 | scissors     | 32.022 | teddy bear     | 48.434 |
| hair drier    | 5.498  | toothbrush   | 32.965 |                |        |


## Evaluation results for segm:  

```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.395
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.624
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.423
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.207
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.423
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.567
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.318
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.488
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.510
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.323
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.547
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.656
```  
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 39.487 | 62.379 | 42.279 | 20.685 | 42.334 | 56.719 |

### Per-category segm AP:  

| category      | AP     | category     | AP     | category       | AP     |
|:--------------|:-------|:-------------|:-------|:---------------|:-------|
| person        | 48.705 | bicycle      | 19.098 | car            | 42.866 |
| motorcycle    | 35.036 | airplane     | 50.918 | bus            | 66.133 |
| train         | 63.987 | truck        | 36.541 | boat           | 24.721 |
| traffic light | 28.909 | fire hydrant | 66.460 | stop sign      | 65.778 |
| parking meter | 47.632 | bench        | 20.251 | bird           | 33.263 |
| cat           | 67.053 | dog          | 62.066 | horse          | 44.417 |
| sheep         | 48.401 | cow          | 52.430 | elephant       | 59.286 |
| bear          | 70.504 | zebra        | 57.114 | giraffe        | 52.413 |
| backpack      | 18.154 | umbrella     | 47.876 | handbag        | 17.271 |
| tie           | 34.437 | suitcase     | 45.231 | frisbee        | 65.789 |
| skis          | 3.721  | snowboard    | 27.591 | sports ball    | 48.027 |
| kite          | 32.761 | baseball bat | 25.987 | baseball glove | 40.982 |
| skateboard    | 33.116 | surfboard    | 34.438 | tennis racket  | 56.696 |
| bottle        | 39.430 | wine glass   | 34.940 | cup            | 45.214 |
| fork          | 21.902 | knife        | 16.068 | spoon          | 14.248 |
| bowl          | 40.363 | banana       | 20.512 | apple          | 22.552 |
| sandwich      | 40.691 | orange       | 32.167 | broccoli       | 21.851 |
| carrot        | 21.073 | hot dog      | 24.350 | pizza          | 51.602 |
| donut         | 51.776 | cake         | 40.673 | chair          | 21.046 |
| couch         | 35.501 | potted plant | 25.443 | bed            | 34.169 |
| dining table  | 17.202 | toilet       | 61.220 | tv             | 60.054 |
| laptop        | 61.569 | mouse        | 59.992 | remote         | 35.393 |
| keyboard      | 51.622 | cell phone   | 38.339 | microwave      | 60.909 |
| oven          | 36.480 | toaster      | 29.480 | sink           | 36.419 |
| refrigerator  | 60.644 | book         | 12.527 | clock          | 53.909 |
| vase          | 40.050 | scissors     | 22.583 | teddy bear     | 45.749 |
| hair drier    | 2.778  | toothbrush   | 20.426 |                |        |
