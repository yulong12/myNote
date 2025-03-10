import requests

# 测试文本嵌入
def test_text():
    url = "http://localhost:8000/embed"
    data = {"modality_type": "text", "text": "a dog playing with a ball"}
    response = requests.post(url, data=data)
    print("Text Embedding:", response.json()["embedding"])

# 测试图像嵌入
def test_image():
    url = "http://localhost:8000/embed"
    files = {"file": open("data/dog_image.jpg", "rb")}
    data = {"modality_type": "vision"}
    response = requests.post(url, files=files, data=data)
    # print("response")
    # print(response)
    print("Image Embedding:", response.json()["embedding"])

# 测试音频嵌入
def test_audio():
    url = "http://localhost:8000/embed"
    files = {"file": open("data/dog_audio.wav", "rb")}
    data = {"modality_type": "audio"}
    response = requests.post(url, files=files, data=data)
    print("Audio Embedding:", response.json()["embedding"])

if __name__ == "__main__":
    test_text()
    test_image()
    test_audio()