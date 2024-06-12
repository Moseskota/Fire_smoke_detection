# Installation

# This script installs necessary packages and mounts Google Drive if running in Colab.

try:
    from torchinfo import summary
except ImportError:
    print("[INFO] Couldn't find torchinfo... installing it.")
    !pip install -q torchinfo
    from torchinfo import summary

from google.colab import drive
drive.mount('/content/drive')
