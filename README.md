# my-photo-enhancer
Restore damaged photos using GFPGAN and Real-ESRGAN with a Streamlit web interface.

## Overview

My Photo Enhancer is a Python web application for restoring old and damaged photographs using state-of-the-art deep learning models. It combines facial restoration, image upscaling, and optional scratch removal through an intuitive Streamlit interface, allowing users to enhance historical or degraded images with minimal effort.

The application provides a simple workflow: upload an image, select the desired restoration options, preview the result with an interactive comparison slider, and download the enhanced version.

## Features

- Face restoration powered by **GFPGAN**
- Optional background enhancement with **Real-ESRGAN**
- Optional scratch and crack removal using **ZeroScratches**
- Interactive before-and-after image comparison
- Download restored images
- Responsive web interface built with Streamlit
- Efficient model loading with caching for improved performance

## Technologies

- Python
- Streamlit
- GFPGAN
- Real-ESRGAN
- ZeroScratches
- OpenCV
- Pillow
- PyTorch

## Installation

Clone the repository and install the required dependencies.

```bash
git clone https://github.com/Tk4liso/my-photo-enhancer.git
cd my-photo-enhancer
pip install -r requirements.txt
```

Start the application with:

```bash
streamlit run app.py
```

## Usage

1. Upload a damaged photograph.
2. Select the desired restoration options.
3. Generate the enhanced image.
4. Compare the original and restored versions using the interactive slider.
5. Download the final result.

## Project Structure

```text
my-photo-enhancer/
├── src/
│   ├── __init__.py
│   ├── model.py      # AI model loading and inference
│   ├── ui.py         # Streamlit interface components
│   └── utils.py      # Helper functions
├── app.py            # Application entry point
├── config.py         # Configuration settings
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Results

The following images show an example of the restoration process performed by the application.

<img width="1600" height="847" alt="image" src="https://github.com/user-attachments/assets/6cbc6636-dd99-466a-993b-73862277a5ee" />

<img width="1001" height="738" alt="image" src="https://github.com/user-attachments/assets/d73b69de-8b70-4890-b95d-835a556849ed" />

<img width="993" height="787" alt="image" src="https://github.com/user-attachments/assets/7f8182f3-1fee-4b2a-90e3-56c6933811a8" />

<img width="1005" height="738" alt="image" src="https://github.com/user-attachments/assets/9d56c404-3f8e-4f15-aabb-c37775665ef5" />

## Acknowledgements

This project builds upon the work of the following open-source projects:

- GFPGAN
- Real-ESRGAN
- ZeroScratches
- Streamlit
