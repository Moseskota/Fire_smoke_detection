# Project Overview

# The goal of this project is to create an effective fire detection system using a pre-trained MobileNetV2 model.
# The system can identify images containing fire or smoke, which is useful for early fire detection in forest and residential areas.

import torch
import torch.nn as nn
from torchvision import models

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Initialize the MobileNetV2 model
mobilenet_v2 = models.mobilenet_v2(pretrained=True)

# Modify the last layer for our specific problem
mobilenet_v2.classifier[1] = nn.Linear(mobilenet_v2.last_channel, 3)  # Assuming 3 classes: fire, smoke, non-fire

# Move the model to the appropriate device
mobilenet_v2 = mobilenet_v2.to(device)
