# Citi-Bike-Trip-ML-Infrastructure

# Bike Sharing Demand Prediction

## Mục tiêu
Xây dựng hệ thống xử lý dữ liệu lớn (>100GB) để dự đoán nhu cầu xe đạp công cộng (Citi Bike) bằng batch và stream processing, phục vụ Machine Learning.

## Công nghệ
- MinIO, Kafka, Flink, Spark, Delta Table, Trino, Airflow
- Triển khai trên Minikube

## Tiến độ
### Ngày 1: Thiết lập Minikube và MinIO
- Cài đặt Minikube.
- Viết file `deploy/minio/deployment.yaml` và `deploy/minio/service.yaml`.
- Kết quả: MinIO chạy trên Minikube, truy cập được qua NodePort.

## Hướng dẫn chạy
1. Khởi động Minikube: `minikube start`
2. Deploy MinIO: `kubectl apply -f deploy/minio/`