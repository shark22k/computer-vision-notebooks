import argparse
import kaggle
from pathlib import Path

def download_kaggle_dataset(dataset_path, output_path):
    """
    Download a dataset from Kaggle and extract it to the specified output directory.
    
    Parameters:
    - dataset_path: str, the Kaggle dataset path in 'user/dataset' format.
    - output_path: Path, the directory where the dataset will be downloaded and extracted.
    """
    # Ensure output directory exists
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading dataset '{dataset_path}' to {output_path}...")
    kaggle.api.dataset_download_files(dataset_path, path=str(output_path), unzip=True)
    print(f"Dataset downloaded and extracted to {output_path}.")

def main():
    parser = argparse.ArgumentParser(description="Download a dataset from Kaggle.")
    parser.add_argument(
        "dataset", type=str, 
        help="The Kaggle dataset path in 'user/dataset' format (e.g., 'balabaskar/tom-and-jerry-image-classification')."
    )
    parser.add_argument(
        "--output", type=str, default="data/",
        help="The directory where the dataset should be downloaded and extracted."
    )
    
    args = parser.parse_args()
    
    dataset_path = args.dataset
    output_path = Path(args.output)
    
    download_kaggle_dataset(dataset_path, output_path)

if __name__ == "__main__":
    main()
