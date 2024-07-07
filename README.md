# Kidney-Disease-Classification-Deep_Learning-DVC-Mlflow
![TUMOR IMAGE](https://github.com/HimanshuRajput013/Kidney_disease_predication_using_deep_learning/assets/131947510/51cddf92-10a5-4987-bfd7-ee0e22586317)
![ML FLOW](https://github.com/HimanshuRajput013/Kidney_disease_predication_using_deep_learning/assets/131947510/2d12bbb8-f515-4e9f-b0cf-c16bcdf15f6d)




## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
[https://github.com/HimanshuRajput013/Kidney_disease_predication_using_deep_learning]
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n env python=3.8 -y
```

```bash
conda activate env
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= \
MLFLOW_TRACKING_USERNAME= \
MLFLOW_TRACKING_PASSWORD= \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/HimanshuRajput013/Kidney_disease_predication_using_deep_learning.mlflow

export MLFLOW_TRACKING_USERNAME=HimanshuRajput013

export MLFLOW_TRACKING_PASSWORD=

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions




