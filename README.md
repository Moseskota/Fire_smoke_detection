# Fire_smoke_detection
This project utilizes the MobileNetV2 architecture for detecting fire in images. The model is trained and evaluated on a dataset of images containing fire, smoke, and non-fire scenes. This project was developed using Google Colab, and it leverages PyTorch for building and training the neural network.

Table of Contents:
Project Overview
Data preprocessing
Model Training
Evaluation




**Project Overview**:
The goal of this project is to create an effective fire detection system using a pre-trained MobileNetV2 model. The system can identify images containing fire or smoke, which is useful for early fire detection in forest and residential areas.

**Dataset**:
The dataset used in this project consists of images categorized into fire, smoke, and non-fire classes. The dataset is stored in a ZIP file and extracted for training and testing.
https://www.kaggle.com/datasets/mosescalvin/forest-fire-smoke-and-non-fire-dataset 

**Model Training**:
The training process involves loading the dataset, preprocessing the images, and training the MobileNetV2 model. The training and validation splits are handled within the script.

**Evaluation** :
The trained model is evaluated using a separate test dataset. The evaluation metrics include loss and accuracy, and a confusion matrix is plotted to visualize the performance of the model.

![Confusion_matrix](https://github.com/Moseskota/Fire_smoke_detection/assets/76688024/94d3efb9-85b8-4b21-88d2-d42eb475e1e1)

