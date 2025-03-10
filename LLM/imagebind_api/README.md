# 1,项目结构
```
.
├── __pycache__
│   └── main.cpython-310.pyc
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── main.cpython-310.pyc
│   ├── imagebind
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── data.cpython-310.pyc
│   │   │   └── data.cpython-312.pyc
│   │   ├── bpe
│   │   │   └── bpe_simple_vocab_16e6.txt.gz
│   │   ├── data.py
│   │   └── models
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-310.pyc
│   │       │   ├── helpers.cpython-310.pyc
│   │       │   ├── imagebind_model.cpython-310.pyc
│   │       │   ├── multimodal_preprocessors.cpython-310.pyc
│   │       │   └── transformer.cpython-310.pyc
│   │       ├── helpers.py
│   │       ├── imagebind_model.py
│   │       ├── multimodal_preprocessors.py
│   │       └── transformer.py
│   ├── main.py
│   ├── models #模型文件
│   │   └── imagebind_weights
│   │       └── imagebind_huge.pth
│   ├── startLocalServer.sh #在本地启动server，用以测试API时用到
│   └── uploads #服务端数据存放目录
│       ├── dog_audio.wav
│       └── dog_image.jpg
├── data
│   ├── dog_audio.wav
│   └── dog_image.jpg
├── docker
│   └── Dockerfile
├── docker-compose.yml
├── image_build.sh
├── image_run.sh
├── imagebind-api.tar
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
├── requirements.txt
└── test_api.py
```