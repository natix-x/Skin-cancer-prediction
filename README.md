# Skin-cancer-prediction - bachelor's thesis
## Table of contents: 
* [General info](#general-info)
* [Setup](#setup-)
* [Data preparation and analysis](#data-preparation-and-analysis)
* [Machine Learning Models](#machine-learning-models)
* [Models evaluation](#models-evaluation)
* [Results and conclusions](#results-and-conclusions)
* [Project status](#project-status)
* [Citation](#citations)

### General info
The aim of this project is to create a machine learning model that predicts to which category a pigmented skin lesion belongs.


### Setup 
The dataset used in this project is obtained from [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T).
To work with this repository download and extract the dataset in 'DATA' directory as shown below:

### Data preparation and analysis

1. Check if dataset is imbalanced or not.
2. Analysis of file 'HAM10000_metadata' - Data overview & distribution plots
3. Classify all available diagnostic categories in the realm of pigmented lesions into three groups: 'melanocytic nevi (nv)', 'melanoma (mel)' and 'other'.
'other' category includes  actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec), basal cell carcinoma (bcc), benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl), dermatofibroma (df) and vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc).

### Machine Learning Models

1. Chosen ML models:
    - Support vector classifier (SVC)

### Models evaluation
### Results and conclusions
### Project status
1. Metadata - EDA.
2. Divide images into subfolders based on their label (diagnosis).
3. Load all images as 1 - dimensional np.array (rgb format) and resize each on them to 150 x 100 pixels
4. Train_test_split (20% - test data)
5. Fit & transform data using StandardScaler
6. Fit PCA to X_train
7. Choose n_components hyperparameter to 150 based on created plot
8. Fit and transform data using PCA (n_components=150)
9. Fit SVC model to X_train (default values of hyperparameters) and evaluate its performance
### Citations

Tschandl, Philipp, 2018, "The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions", https://doi.org/10.7910/DVN/DBW86T, Harvard Dataverse, V4, UNF:6:KCZFcBLiFE5ObWcTc2ZBOA== [fileUNF]



