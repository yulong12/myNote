# 使用官方Python基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /imagebind_api

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY app/imagebind ./app/imagebind
COPY app/uploads ./app/uploads
COPY app/__init__.py ./app/
COPY app/main.py    ./app/
COPY app/models/imagebind_weights   ./app/models/imagebind_weights

WORKDIR /imagebind_api/app
# 暴露API端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]