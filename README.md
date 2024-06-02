# Skin-cancer-prediction
## Table of contents: 
* [General info](#general-info)
* [Setup](#setup)
* [Requirements](#requirements)
* [Data preparation and analysis](#data-preparation-and-analysis)
* [Machine Learning](#machine-learning)
* [Deep Learning](#deep-learning)
* [Final Model](#final-model)
* [Web Application](#web-application)
* [Citation](#citations)

### General info
The aim of this project is to create a simple web application using Flask for deploying a Convolutional Neural Network (CNN) model that classifies skin lesions into 7 different categories. This project focuses on building the most accurate Keras Sequential model without using transfer learning for better understanding neural networks and their learning process. The web app is designed to be as user-friendly and straightforward as possible.
### Setup
The dataset used in this project is obtained from [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T).
To work with this repository download and extract the dataset in 'DATA' directory as shown below:
```sh
     DATA/
    ├── HAM10000_images_part_1_and_2
    │   ├── ISIC_00000000.jpg
    │   └── 
    └── HAM10000_metadata
   ```
Put all images into 'HAM10000_images_part_1_and_2' directory.
### Requirements
* Python 3.11+
* As each part (data analysis, data modelling and app) could be explored separately, for each part is created file 'requirements.txt' that contains a list of packages or libraries needed to work on selected part
* 'requirements.txt' outside listed part directories contains packages needed for all parts
### Data preparation and analysis
1. Metadata analysis.
2. Categories to which lesions are classified are listed below:
   * nv - melanocytic nevi
   * mel - melanoma
   * akiec - actinic keratoses and Bowen's disease
   * bcc - basal cell carcinoma
   * bkl - benign keratosis-like lesions
   * df - dermatofibroma
   * vasc - vascular lesions

### Machine Learning

... in progress ...

### Deep learning
Chosen neural network: CNN
1. Creation of a simple model architecture in order to see how it performs on extremely imbalanced dataset. 
   * high accuracy already at the begging 
   * extremely low 'recall' and 'F1-score' values
   * model predicts almost all lesions to be 'nv' (major class)
   
<img src="DATA/plots/confusion_matrix_unchanged_dataset_first_model.png" alt="drawing" style="width:300px;"/>

2. Adding class weights while training -> really low accuracy
3. Balance train data - usage of RandomOverSampler and RandomUnderSampler in order to have 1000 samples of each class
4. Trying different model architectures. 
5. Saving the best model found while searching for best values of hyperparameters using KerasTuner(creation of the class CNNHyperModel that inherits from HyperModel).
6. Cloning the architecture of bets model, fits train data to it, make use of callbacks (early stopping if model's accuracy on validation data does not improved since 8 epochs).
7. Final evaluation of the model.
8. Saving final model (.keras format)
### Final Model
Model architecture:
![architecture](DATA/plots/CNN_final_model_architecture.png)
Confusion matrix:

<img src="DATA/plots/confusion_matrix_balanced_dataset_final_model.png" alt="drawing" style="width:300px;"/>

Accuracy: 70%
### Web Application

### Citations
Tschandl, Philipp, 2018, "The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions", https://doi.org/10.7910/DVN/DBW86T, Harvard Dataverse, V4, UNF:6:KCZFcBLiFE5ObWcTc2ZBOA== [fileUNF]



