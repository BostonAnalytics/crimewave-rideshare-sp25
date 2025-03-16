import gdown
import os

# Define Google Drive file IDs and output paths
drive_links = {
    "rideshare": "1-nx0DfC7XMSoZDeY1LeWXw3lHewl5iLv",
    "crime": "1AAX-Z4AhXU0EWAVcFpfYQ1HRTkYNggs6"
}

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

for name, file_id in drive_links.items():
    output_path = os.path.join(data_dir, f"{name}_data.parquet")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)