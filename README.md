# Fire_smoke_detection
This project utilizes the MobileNetV2 architecture for detecting fire in images. The model is trained and evaluated on a dataset of images containing fire, smoke, and non-fire scenes. This project was developed using Google Colab, and it leverages PyTorch for building and training the neural network.

Table of Contents:
Project Overview
Data preprocessing
Model Training
Evaluation
Results
Contributors
License



Project Overview
The goal of this project is to create an effective fire detection system using a pre-trained MobileNetV2 model. The system can identify images containing fire or smoke, which is useful for early fire detection in forest and residential areas.

Dataset
The dataset used in this project consists of images categorized into fire, smoke, and non-fire classes. The dataset is stored in a ZIP file and extracted for training and testing.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/fire_detection_mobilenet.git
cd fire_detection_mobilenet
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Download the dataset and place it in the appropriate directory as specified in the script.

Usage
To use the script, ensure that you have the dataset in the correct path and then run the script using Python:

bash
Copy code
python fire_detection_mobilenet.py
Model Training
The training process involves loading the dataset, preprocessing the images, and training the MobileNetV2 model. The training and validation splits are handled within the script.

Evaluation
The trained model is evaluated using a separate test dataset. The evaluation metrics include loss and accuracy, and a confusion matrix is plotted to visualize the performance of the model.
