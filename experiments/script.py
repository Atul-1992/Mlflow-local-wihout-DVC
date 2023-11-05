from pathlib import Path
from random import random

import mlflow


def main():
    mlflow.set_tracking_uri("http://mlflow:5000")
    experiment_name = "playground"

    try:
        mlflow.create_experiment(experiment_name)
    except mlflow.exceptions.RestException:  # type: ignore
        pass

    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        mlflow.log_param("test", 13)

        mlflow.log_metric("foo", random())
        mlflow.log_metric("foo", random() + 1)
        mlflow.log_metric("foo", random() + 2)

        # Define the name of the artifact file
        artifact_filename = "tmp.txt"

        # Construct the full path within the 'mlflow/artifacts' directory
        artifact_path = Path(__file__).parents[1]/'mlflow'/'artifacts'/ artifact_filename
        # artifact_path = os.path.join("mlflow/artifacts", artifact_filename)

        # Write content to the artifact file
        artifact_path.write_text("Everything is working!")

        # Log the artifact to MLflow
        mlflow.log_artifact(artifact_path)


if __name__ == "__main__":
    main()