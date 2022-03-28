# Object Detection in an Urban Environment

## Submission Template

### Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?
 →If no object is detected, the object will be ignored and the vehicle will run. As a result, it collides with an object.

### Set up
This section should contain a brief description of the steps to follow to run the code for this repository.
 →Please see "README.md".

### Dataset
#### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.
 →You can visualize the dataset with Exploratory Data Analysis.ipynb.
   There are various things such as bright images and dark images, but you can see that they are all images taken by the camera mounted on the car traveling on the road.
   In other words, you can see that there are many vehicles that you want to detect in the center and bottom of the image.
#### Cross validation
This section should detail the cross validation strategy and justify your approach.
 →I split Train_Data, Test_Data and Val_Data into 8: 1: 1.
   This is to perform learning with high accuracy by using as much data as possible for learning.

### Training
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

The result of the Reference experiment is stored in the "chart_before" folder.

・ DetectionBoxes_Precisio  The file name is "Before_1.DetectionBoxes_Precision.png".
Since the plot at 2.5k is interrupted, this time we will compare with Precision at 2k.
-DetectionBoxes_Precision / mAP 		=.8e-3
-DetectionBoxes_Precision / mAP (larg 	= 7e-4
-DetectionBoxes_Precision / mAP (medi) 	= 0.014
-DetectionBoxes_Precision / mAP (sml) 	= 2.6e-3
-DetectionBoxes_Precision / mAP50IOU 	= 0.012
-DetectionBoxes_Precision / mAP@.75IOU 	= 3.7e-3
  
・ DetectionBoxes_Recall
The file name is "Before_2.DetectionBoxes_Recall.png".
Since the plot at 2.5k is also interrupted, this time we will compare with Recall at 2k.
-DetectionBoxes_Recall / AR @ 1 			= 4.4e-3
-DetectionBoxes_Recall / AR @ 10 			= 0.14
-DetectionBoxes_Recall / AR @ 100 			= 0.33
-DetectionBoxes_Recall / AR @ 100 (large) 	= 0.042
-DetectionBoxes_Recall / AR @ 100 (medium) 	= 0.78
-DetectionBoxes_Recall / AR @ 100 (small) 	= 0.016

・ Loss
The file name is "Before_3.Loss.png".
Loss focuses on converged values.
-Loss / classification_loss 	= 0.45
-Loss / localization_loss 		= 0.54
-Loss / normalized_total_loss 	= 16
-Loss / regularization_loss 	= 15
-Loss / total_loss 				= 16

・ Learning_rate
The file name is "Before_4.learning_rate.png".
Since this parameter has been changed to improve accuracy, the values before the change of the parameters related to this chart are described.
I will describe the changed value later.
-learning_rate_base		: 0.04
-total_steps			: 2500
-warmup_learning_rate	: 0.013333
-warmup_steps			: 200

・ Steps_per_sec
The file name is "Before_5.steps_per_sec.png".
You can check how the learning is stable.

#### Improve on the reference
Looking at the change in learning Loss before the model change (Before_3.Loss.png), we can see that Loss has converged before it converged to 0.
Therefore, we aimed to converge with a lower loss by lowering the learning rate.
We also predicted that lowering the learning rate would increase the step required for loss convergence.
Therefore, we aimed to converge loss in a limited environment by increasing total_steps and warmup_steps.

The results of the improved reference experiment are saved in the "chart_after" folder.

・ DetectionBoxes_Precision
The file name is "After_1.DetectionBoxes_Precision.png".
The plot started from a strange place, probably because the previous file remains, but you can see that we were able to re-evaluate by moving to 0step.
Since the plot before the model change is interrupted at 2.5k, this time we will compare with Precision at 2k.
If the accuracy is improved, it is described as "improved", if it is decreased, it is described as "decline", and if it does not change, it is described as "same".
-DetectionBoxes_Precision / mAP 			= .8e-3 (same)
-DetectionBoxes_Precision / mAP (large) 	= 0.08 (improved)
-DetectionBoxes_Precision / mAP (medium) 	= 0.018 (improved)
-DetectionBoxes_Precision / mAP (small) 	= 1e-3 (decline)
-DetectionBoxes_Precision / mAP@.50IOU 		= 0.025 (improved)
-DetectionBoxes_Precision / mAP@.75IOU 		= 3.9e-3 (improved)
  
・ DetectionBoxes_Recall
The file name is "After_2.DetectionBoxes_Recall.png".
This is also probably because the previous file remains, the plot started from a strange place, but you can see that it was possible to re-evaluate by moving to 0step.
Also, since the plot before the model change is interrupted at 2.5k, this time we will compare with Precision at 2k.
If the accuracy is improved, it is described as "improved", if it is decreased, it is described as "decline", and if it does not change, it is described as "same".
-DetectionBoxes_Recall / AR @ 1 			= 3.6e-3 (decline)
-DetectionBoxes_Recall / AR @ 10 			= 0.014 (same)
-DetectionBoxes_Recall / AR @ 100 			= 0.038 (improved)
-DetectionBoxes_Recall / AR @ 100 (large) 	= 0.26 (improved)
-DetectionBoxes_Recall / AR @ 100 (medium) 	= 0.08 (improved)
-DetectionBoxes_Recall / AR @ 100 (small) 	= 0.011 (decline)

・ Loss
The file name is "After_3.Loss.png".
loss is compared by the converged value.
If the accuracy is improved, it is described as "improved", if it is decreased, it is described as "decline", and if it does not change, it is described as "same".
-loss / classification_loss 	= 0.41 (improved)
-loss / localization_loss 		= 0.5 (improved)
-loss / normalized_total_loss 	= 1.4 (improved)
-loss / regularization_loss 	= 0.485 (improved)
-loss / total_loss 				= 1.4 (improved)

・ Learning_rate
The file name is "After_4.learning_rate.png".
You can see that the changes were made as intended.
-learning_rate_base		: 0.03
-total_steps			: 3000
-warmup_learning_rate	: 0.013333
-warmup_steps			: 500

・ Steps_per_sec
The file name is "After_5.steps_per_sec.png".
You can confirm that the learning is stable this time as well.