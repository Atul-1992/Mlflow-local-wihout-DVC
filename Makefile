include .envs/.mlflow-common
include .envs/.experiments
include .envs/.mlflow-dev
include .envs/.postgres
export

build:
	docker compose build

build-server:
	docker compose build mlflow

up:
	docker compose up -d

down:
	docker compose down

experiment:
	docker compose up -d experiments

exec-server:
	docker compose exec mlflow-server /bin/bash

inter-server:
	docker compose exec -it mlflow /bin/bash