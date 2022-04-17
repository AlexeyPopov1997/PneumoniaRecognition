# Pneumonia Recognition

#### A simple application for recognition area of lung involvement in pneumonia on fluorography scans.
The application was created as part of the Data Integration in Information Systems Course.

When creating a determining pneumonia model, the **[Mask R-CNN](https://github.com/matterport/Mask_RCNN)** model was used.
The implementation of the model and its description can be found here: **[model_description.ipynb](https://gitlab.com/AlexeyPopov1997/pneumonia-recognition/-/blob/main/notebook/model_description.ipynb)**.

![readme](/pictures/readme.gif)

## Dataset
The dataset taken from here: **[RSNA Pneumonia Detection Challenge](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge)**.

## Instalation a virtual environment
1. Clone the repository:
```sh
git clone https://gitlab.com/AlexeyPopov1997/pneumonia-recognition.git
```
2. Download the model from the link: **???**
3. Copy model to folder: **???**

***
*If you wish, you can easily create your own model using **[model_description.ipynb](https://gitlab.com/AlexeyPopov1997/pneumonia-recognition/-/blob/main/notebook/model_description.ipynb)***
***

4. Next, create a virtual environment using the file **[environment.yml](https://gitlab.com/AlexeyPopov1997/pneumonia-recognition/-/blob/main/environment.yml)** (**Don't forgive to change `prefix` in the file!**):
```sh
conda env create -f environment.yml
```

## Usage
1. Activate the environment:
```sh
conda activate PneumoniaRecognition
```
2. Run the application:
```sh
python main.py
```

## Authors and acknowledgment
1. [Mask-RCNN and COCO transfer learning LB:0.155](https://www.kaggle.com/hmendonca/mask-rcnn-and-coco-transfer-learning-lb-0-155)
2. [R-CNN – Neural Network for Object Detection and Semantic Segmentation](https://neurohive.io/en/popular-networks/r-cnn/)
3. [The complete PyQt5 tutorial — Create GUI applications with Python](https://www.learnpyqt.com/)