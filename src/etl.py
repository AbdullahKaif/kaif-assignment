import pandas as pd
import argparse
import os

def process_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.fillna(0)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    parser.add_argument("--output_path")
    args = parser.parse_args()
    process_data(args.input_path, args.output_path)