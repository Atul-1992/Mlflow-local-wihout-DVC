create-mlflow-server:
	docker compose build

start-mlflow-server:
	docker compose up -d

stop-mlflow-server:
	docker compose down

run-experiments:
	docker run -it --name mlflow -v /experiments:/app bitnami/mlflow:latest script.py