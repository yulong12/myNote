import sys
import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import torch
from pathlib import Path
import shutil
sys.path.append(str(Path(__file__).parent / "imagebind"))
from imagebind import data
from imagebind.models import imagebind_model
from imagebind.models.imagebind_model import ModalityType
# 初始化FastAPI
app = FastAPI()

# 配置参数
MODEL_DIR = "./models/imagebind_weights"
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# 加载模型（服务启动时加载一次）
@app.on_event("startup")
async def load_model():
    global model
    model = imagebind_model.imagebind_huge(pretrained=False)
    model.load_state_dict(torch.load(os.path.join(MODEL_DIR, "imagebind_huge.pth")))
    model.eval().to(DEVICE)
    print("✅ Model loaded successfully")

@app.post("/embed")
async def get_embeddings(
    modality_type: str = Form(...),
    file: UploadFile = File(None),
    text: str = Form(None),
):
    print("---------modality type--------"+modality_type)
    try:
        inputs = {}
        # 根据模态类型处理输入
        if modality_type == ModalityType.TEXT:
            inputs = {ModalityType.TEXT: data.load_and_transform_text([text], DEVICE)}
        elif modality_type == ModalityType.VISION:
            file_bytes = await file.read()
            UPLOAD_DIR = Path() / "uploads"
            UPLOAD_DIR.mkdir(exist_ok=True)
            save_path = UPLOAD_DIR / file.filename
            with open(save_path,"wb") as f:
                f.write(file_bytes)

            inputs = {ModalityType.VISION: data.load_and_transform_vision_data([save_path], DEVICE)}
        elif modality_type == ModalityType.AUDIO:
            file_bytes = await file.read()
            UPLOAD_DIR = Path() / "uploads"
            UPLOAD_DIR.mkdir(exist_ok=True)
            save_path = UPLOAD_DIR / file.filename
            with open(save_path,"wb") as f:
                f.write(file_bytes)

            inputs = {ModalityType.AUDIO: data.load_and_transform_audio_data([save_path], DEVICE)}
        else:
            return JSONResponse(
                {"error": f"Unsupported modality: {modality_type}"}, status_code=400
            )
        # 推理
        with torch.no_grad():
            embeddings = model(inputs)
        return JSONResponse({
            "modality": modality_type,
            "embedding": embeddings[modality_type].cpu().numpy().tolist()
        })
    
    except Exception as e:
        return JSONResponse(
            {"error": str(e)}, status_code=500
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)