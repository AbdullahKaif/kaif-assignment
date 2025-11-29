MLOps Assignment: End-to-End Housing Price Prediction Pipeline
Course: Cloud MLOps (BS AI)
Assignment: #4

📌 Project Overview

This project implements a robust Machine Learning Operations (MLOps) pipeline to predict California Housing prices using a Random Forest Regressor.

The pipeline focuses on reproducibility, automation, and experiment tracking. It creates a seamless workflow from raw data ingestion to model training and evaluation, orchestrating distinct steps into a cohesive lifecycle.

🛠️ Tech Stack & Architecture

This project adapts industry-standard tools to create a lightweight, reproducible environment on macOS:

Component

Tool Used

Purpose

Orchestration

MLflow Projects

Replaces Kubeflow to manage the pipeline workflow and parameter logging locally.

Data Versioning

DVC (Data Version Control)

Tracks large datasets and ensures data lineage (simulated S3 bucket locally).

Model Training

Scikit-Learn

Random Forest Regressor for tabular data prediction.

CI/CD

GitHub Actions

Replaces Jenkins to automatically test code syntax and dependencies on every push.

Language

Python 3.9+

Core scripting language.

📂 Project Structure

├── .github/workflows
│   └── ci.yml             # CI/CD pipeline configuration (GitHub Actions)
├── data/
│   ├── raw_data.csv       # Versioned input dataset (Tracked by DVC)
│   └── processed_data.csv # Generated output from ETL step
├── src/
│   ├── etl.py             # Script: Data extraction, cleaning, and splitting
│   ├── train.py           # Script: Model training and RMSE calculation
│   └── main.py            # Driver script connecting ETL and Training steps
├── MLproject              # MLflow definition file (Entry points & Parameters)
├── requirements.txt       # Project dependencies
├── Dockerfile             # Container configuration
└── README.md              # Project documentation


🚀 How to Run the Project

1. Prerequisites

Ensure you have Python 3 installed. It is recommended to run this inside a virtual environment.

# Clone the repository
git clone [https://github.com/AbdullahKaif/kaif-assignment.git](https://github.com/AbdullahKaif/kaif-assignment.git)
cd kaif-assignment

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


2. Data Setup (DVC)

The data is versioned using DVC. To ensure you have the correct data version linked to the current code commit:

# Pull the latest data version from remote storage
dvc pull


3. Execute the Pipeline

Run the entire pipeline (ETL + Training) using MLflow. This command uses the MLproject file to stitch the steps together.

# Run using the local environment
mlflow run . --env-manager=local


4. View Results (UI)

To visualize the experiments, compare runs, and see the RMSE metrics and Artifacts:

# Start the MLflow UI server
mlflow ui


Then open your browser to http://127.0.0.1:5000

⚙️ Pipeline Components

Stage 1: ETL (src/etl.py)

Input: Raw CSV data (data/raw_data.csv).

Process: Handles missing values and prepares the dataset structure.

Output: Saves the clean dataset to data/processed_data.csv.

Stage 2: Training (src/train.py)

Input: Processed data from the previous step.

Process:

Splits data into Train/Test sets.

Trains a RandomForestRegressor (Estimators: 50).

Calculates Root Mean Squared Error (RMSE).

Logging: Uses mlflow.autolog() to automatically capture parameters, metrics, and the trained model file.

🤖 CI/CD Automation

The project uses GitHub Actions for Continuous Integration.

Trigger: Pushes to the main branch.

Jobs:

Sets up an Ubuntu runner.

Installs Python dependencies.

Performs syntax checks (--help) on etl.py and train.py to ensure code validity before deployment.
