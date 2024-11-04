import os
import zipfile
from pathlib import Path
import requests
import argparse

def download_and_extract_data(url, data_path="data", folder_name="pizza_steak_sushi"):
    """
    Download and extract a ZIP dataset from a specified URL.
    
    Parameters:
    - url: str, the URL to download the dataset from.
    - data_path: str, the base directory for saving data.
    - folder_name: str, the folder name for extracted data.
    """
    # Setup path to data folder
    data_path = Path(data_path)
    image_path = data_path / folder_name

    # Check if image folder already exists
    if image_path.is_dir():
        print(f"{image_path} directory exists.")
    else:
        print(f"Did not find {image_path} directory, creating one...")
        image_path.mkdir(parents=True, exist_ok=True)

        # Download the zip file
        zip_file_path = data_path / f"{folder_name}.zip"
        with open(zip_file_path, "wb") as f:
            print(f"Downloading data from {url}...")
            request = requests.get(url)
            f.write(request.content)
        
        # Unzip the downloaded file
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            print(f"Unzipping data to {image_path}...")
            zip_ref.extractall(image_path)
        
        # Remove the zip file
        os.remove(zip_file_path)
        print(f"Removed zip file: {zip_file_path}")

def main():
    parser = argparse.ArgumentParser(description="Download and extract dataset from URL.")
    parser.add_argument(
        "url",
        type=str,
        help="The URL of the dataset zip file to download."
    )
    parser.add_argument(
        "--data_path",
        type=str,
        default="data",
        help="The base directory for saving data (default: 'data')."
    )
    parser.add_argument(
        "--folder_name",
        type=str,
        default="image_data,
        help="The folder name for extracted data (default: 'pizza_steak_sushi')."
    )

    args = parser.parse_args()
    download_and_extract_data(url=args.url, data_path=args.data_path, folder_name=args.folder_name)

if __name__ == "__main__":
    main()
