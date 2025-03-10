docker run -d \
  --gpus all \
  -p 8000:8000 \
  -v ./app/models:/app/models \
  --name imagebind-api \
  imagebind-api:1.0
