
# Person Fall Detection

This repo is the workspace dedicated to the Task 1 of the Yavar.ai internship assessment.

# Problem Statement

People’s Fall is a serious concern especially since it is life threatening sometimes.
Hence we need a solution that generally identifies fall of people and specifically at
staircases, escalators, steps etc.

Library/Algorithms to use: YOLO CV Library

Input: Offline Videos in mp4 format
Evaluation Criteria
- High level of Accuracy of predictions
- Extremely low False Positives

# How it works
Data Collection: We leverage an open-source image dataset to fine-tune our model for fall detection.

Preprocessing: Images are resized to match the input requirements of the chosen model, ensuring compatibility. Additionally, data augmentation techniques can be employed to artificially increase the dataset size and improve model robustness.

Frame-by-Frame Analysis: The video file is converted into a sequence of individual frames, each one fed into the fine-tuned model for fall detection.

Here is the brief overview of Data Flow



![Flow](/assets/flow.png)
---
# Model Overview

In the current design we use a combination of the [PoseNet 2.0](https://github.com/tensorflow/tfjs-models/tree/master/posenet) Deep Neural Network model and domain specific heuristics to estimate a fall occurance. 

Below are the key points that posenet is capable of identifying 


![Posenet](/assets/posnet_keypoints.png)
---
The preprocessed dataset is used to fine-tune PoseNet, enhancing its ability to detect falls within our specific domain.

Key body joint angles, like the knee angle, are monitored. Sudden changes in these angles, such as a sharp drop in the knee angle, can be indicative of a fall event.


The following diagram illustates the main steps.


[![Model Working](https://user-images.githubusercontent.com/2234901/112545190-ea89d380-8d85-11eb-8e2c-7a6b104d159e.png)](https://drive.google.com/file/d/1sr2OcEWsGzoxJb4PwCIXOuEo7a5ubAxG/view?usp=sharing)

# Evaluation
Reveived an accuracy of 92.8%

# Experiment

Experiment with the fall-detection module using simple script

###### Run a Python Script

```
python demo-fall-detection.py
```


# Limitations

Based on testing, following are the limitations for the Fall Detection algorithm:

- Distance from monitored area: Optimal about 15-25 feet (5-8 meters). The camera has to be able to see the whole person in standing position before the fall and fallen position after the fall. If the camera is not able to see a substantial part of the body, the Fall Detection model may not have sufficient confidence in its estimation of the situation.
- Camera hight: Optimal at about human eye level: about 4-7ft (1-2 meters). If the camera is angled too low or too high overhead , the PoseNet model is not able to estimate body keypoints with confidence.
- Lighting condition: Good lighting is required for optimal performance. Dim light reduces PoseNet's confidence in keypoint estimates.
- Single person: The model is optimized for situation when a person is home alone. If there are multiple people in the camera view, that may confuse the model and lead to false fall detections.
- No clutter: The model performs best when the area being monitored is relatively clear of various small objects. Areas cluttered with objects may confuse the model that some of these objects look like people.
- Occlusions: The model suffers when the person falls behind furniture (e.g. a table or a chair) that blocks the camera from seeing a substantial part of the body.
