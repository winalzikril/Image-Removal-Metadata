# Image-Removal-Metadata
This Python script provides a graphical user interface (GUI) for removing metadata from image files. It uses the Tkinter library for creating the GUI, and the Pillow (PIL) library to open, process, and save images. The application allows users to select an input image, choose an output location, and remove metadata from the image. 

# Image Metadata Remover

## Overview

This Python script provides a simple graphical user interface (GUI) for removing metadata from image files. It allows you to select an input image, remove its metadata, and save the resulting image with an additional "metnew" label in the filename. The script is useful for preserving privacy or reducing file size when sharing images.

## Prerequisites

Before using this script, make sure you have Python 3.x installed on your system. You'll also need to install the following Python libraries:

- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/index.html) for image processing:

  ```bash
  pip install Pillow

How to Use
Clone or download this repository to your local machine.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script:
python remove_metadata_gui.py

The GUI window will appear, allowing you to perform the following steps:

Click the "Browse" button next to "Input Image" to select the image file from which you want to remove metadata.

The "Output Image" field will be automatically populated with the new filename, including the "metnew" label. You can change this filename if needed.

Click the "Remove Metadata" button to process the image and save it with metadata removed.

The status label will display messages about the process, including success or error messages.

The processed image will be saved in the same directory with the modified filename.

Acknowledgments
Special thanks to the Pillow library for image processing.
This project was inspired by the need to remove metadata from images for privacy and sharing purposes.
