import mlflow
import argparse

def workflow(raw_data):
    with mlflow.start_run(run_name="Main Pipeline"):
        print(">>> Running ETL")
        mlflow.run(".", "etl", 
            parameters={"input_file": raw_data, "output_file": "data/processed_data.csv"},
            env_manager="local"
        )

        print(">>> Running Training")
        mlflow.run(".", "train", 
            parameters={"data_file": "data/processed_data.csv", "n_estimators": 50},
            env_manager="local"
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_data")
    args = parser.parse_args()
    workflow(args.raw_data)