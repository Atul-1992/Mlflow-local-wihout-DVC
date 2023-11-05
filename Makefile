create-mlflow-server:
	docker compose build

start-mlflow-server:
	docker compose up -d

stop-mlflow-server:
	docker compose down

run-experiments:
	docker compose up -d experiments