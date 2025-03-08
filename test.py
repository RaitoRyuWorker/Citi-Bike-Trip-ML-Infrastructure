import boto3
from botocore.client import Config

# Cấu hình MinIO
minio_url = "http://192.168.49.2:30000"  # Thay bằng URL từ `minikube service`
access_key = "admin"
secret_key = "password"
bucket_name = "raw-data"

# Kết nối MinIO
s3_client = boto3.client('s3',
    endpoint_url=minio_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    config=Config(signature_version='s3v4')
)

# Tạo bucket nếu chưa có
# s3_client.create_bucket(Bucket=bucket_name)

# Upload file thử nghiệm
s3_client.upload_file("temp.txt", bucket_name, "temp.txt")
print("Uploaded successfully!")