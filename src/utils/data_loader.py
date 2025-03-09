import requests
import boto3
from botocore.client import Config
import os

# MinIO
MINIO_URL = "http://192.168.49.2:30000"  # API port from minikube ip
ACCESS_KEY = "admin"
SECRET_KEY = "password"
BUCKET_NAME = "raw-data"

# MinIO Connection
s3_client = boto3.client('s3',
    endpoint_url=MINIO_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4')
)

def download_file(url, local_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded {local_path}")
    else:
        print(f"Failed to download {url}")

def upload_to_minio(local_path, minio_path):
    try:
        s3_client.upload_file(local_path, BUCKET_NAME, minio_path)
        print(f"Uploaded {minio_path} to MinIO")
    except Exception as e:
        print(f"Error uploading {minio_path}: {e}")

def load_citibike_data():
    citibike_url = "https://s3.amazonaws.com/tripdata/JC-202502-citibike-tripdata.csv.zip"
    local_path = "data/citibike/JC-202502-citibike-tripdata.csv.zip"
    minio_path = "citibike/JC-202502-citibike-tripdata.csv.zip"

    os.makedirs("data/citibike", exist_ok=True)

    download_file(citibike_url, local_path)
    upload_to_minio(local_path, minio_path)

if __name__ == "__main__":
    try:
        s3_client.create_bucket(Bucket=BUCKET_NAME)
        print(f"Created bucket {BUCKET_NAME}")
    except s3_client.exceptions.BucketAlreadyExists:
        print(f"Bucket {BUCKET_NAME} already exists")
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket {BUCKET_NAME} is already owned by you")

    load_citibike_data()