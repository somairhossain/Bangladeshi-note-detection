import os
os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "0"
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from ultralytics import YOLO
from PIL import Image
import io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = YOLO(os.path.join(BASE_DIR, "model", "best.pt"))

app = FastAPI()


@app.post("/predict")
async def predict(file : UploadFile = File(...)):

    content = await file.read()
    image = Image.open(io.BytesIO(content))
    results = model(image)

    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "class" : result.names[int(box.cls)],
                "confidence" : float(box.conf),
                "bbox" : box.xyxy.tolist()
            })

    return{
        "filename" : file.filename,
        "detections" : detections,
        "total_detected" : len(detections)
    }