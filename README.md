# Bangladeshi Taka Note Detection API

A REST API for detecting and classifying Bangladeshi Taka banknotes using a YOLOv8 object detection model, served with FastAPI and containerized with Docker.

---
* deployed on cloud on render*
* web link
 [Bangladeshi-note-detection](https://bangladeshi-note-detection.onrender.com/)
  
## Project Structure

```
taka-detection-project/
├── Dockerfile          # Docker image definition
├── main.py             # FastAPI application
├── requirements.txt    # Python dependencies
└── model/
    └── best.pt         # Trained YOLOv8 model weights
```

---

## Requirements

- [Docker](https://www.docker.com/) installed on your machine
- No Python installation needed — everything runs inside the container

---

## Getting Started

### 1. Clone or download the project

```bash
git clone <your-repo-url>
cd Ai_Eng_Assignment_17
```

### 2. Build the Docker Image

Run the following command from inside the `taka-detection-project/` directory:

```bash
docker build -t taka-detector .
```

This will:
- Pull the `python:3.11-slim` base image
- Install all required Python packages
- Copy the source code and model weights into the container

### 3. Run the Docker Container

```bash
docker run -d -p 8000:8000 --name taka-api taka-detector
```

| Flag | Description |
|------|-------------|
| `-d` | Run in detached (background) mode |
| `-p 8000:8000` | Map container port 8000 to host port 8000 |
| `--name taka-api` | Name the container for easy reference |

The API will be available at: `http://localhost:8000`

---

## Using the API

### Endpoint

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/predict` | Upload an image and get detection results |

### Request

- **Content-Type:** `multipart/form-data`
- **Field:** `file` — a JPEG or PNG image of Bangladeshi Taka notes

### Response (JSON)

```json
{
  "filename": "taka_sample.jpg",
  "detections": [
    {
      "class": "500",
      "confidence": 0.934,
      "bbox": [[120.5, 80.3, 410.2, 300.7]]
    }
  ],
  "total_detected": 1
}
```

| Field | Description |
|-------|-------------|
| `class` | Detected denomination (e.g. 100, 500, 1000) |
| `confidence` | Model confidence score (0 to 1) |
| `bbox` | Bounding box coordinates `[x1, y1, x2, y2]` |

---

## Testing with Postman

1. Open Postman and create a new **POST** request
2. Set the URL to `http://localhost:8000/predict`
3. Go to **Body** → select **form-data**
4. Add a key named `file`, change its type to **File**
5. Upload a test image and click **Send**
<img width="419" height="335" alt="Screenshot 2026-04-17 143633" src="https://github.com/user-attachments/assets/1301bfd7-8b4d-4ac2-9416-da54045be855" />
<img width="361" height="333" alt="Screenshot 2026-04-17 143725" src="https://github.com/user-attachments/assets/2ebae689-51cc-44bb-ad2f-996581f277ec" />
<img width="396" height="345" alt="Screenshot 2026-04-17 143859" src="https://github.com/user-attachments/assets/a57c43fe-8a4e-4ba0-9797-3a5d98f7d738" />
<img width="414" height="711" alt="Screenshot 2026-04-17 143954" src="https://github.com/user-attachments/assets/4e424306-ccb6-427c-b9bc-6e8f278f5bec" />
<img width="385" height="336" alt="Screenshot 2026-04-17 142755" src="https://github.com/user-attachments/assets/3adad86b-1cf2-4579-87de-9d2f6c87d879" />

## Testing with curl

```bash
curl -X POST http://localhost:8000/predict \
  -F "file=@/path/to/your/image.jpg"
```

---

## Useful Docker Commands

```bash
# View running containers
docker ps

# View container logs
docker logs taka-api

# Stop the container
docker stop taka-api

# Remove the container
docker rm taka-api

# Remove the image
docker rmi taka-detector
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `fastapi` | Web framework for building the REST API |
| `uvicorn` | ASGI server to run the FastAPI app |
| `ultralytics` | YOLOv8 model inference |
| `pillow` | Image loading and processing |
| `python-multipart` | Handling file uploads in FastAPI |
| `opencv-python-headless` | Image operations without display dependencies |

---

## Notes

- The model expects clear, well-lit images of Bangladeshi Taka notes for best accuracy.
- Invalid or corrupt image files will return an appropriate HTTP error response.
- The API runs on port `8000` by default inside the container.
