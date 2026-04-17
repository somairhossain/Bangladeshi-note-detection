FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fix OpenCV headless issue
RUN pip uninstall -y opencv-python opencv-python-headless && \
    pip install --no-cache-dir opencv-python-headless

COPY . .

ENV QT_QPA_PLATFORM=offscreen
ENV OPENCV_IO_ENABLE_OPENEXR=0

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]