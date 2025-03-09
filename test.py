import boto3
from botocore.client import Config
import requests


url = "https://s3.amazonaws.com/tripdata/JC-202502-citibike-tripdata.csv.zip"
local_path = "data/citibike/JC-202502-citibike-tripdata.csv.zip"

response = requests.get(url, stream=True)
print(response.status_code)
if response.status_code == 200:
    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f"Downloaded {local_path}")