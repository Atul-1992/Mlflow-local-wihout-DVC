# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install mlflow

# Expose the port for the MLflow server (default is 5000)
EXPOSE 5000

# Define the command to run your MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0"]
