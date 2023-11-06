#!usr/bin/bash

mlflow server \
    --host 0.0.0.0 \
    --backend-store-uri postgresql://mlflow:mlflow@postgres/mlflow \
    --default-artifact-root ./mlflow/artifacts