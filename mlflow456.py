import dagshub
dagshub.init(repo_owner='HimanshuRajput013', repo_name='Kidney_disease_predication_using_deep_learning', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)