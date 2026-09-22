# Trash Detection App 🗑️

This repository contains a simple Python script to run an object detection model that identifies trash in images. The model was trained using **Roboflow** and utilizes a **YOLOv11** architecture.

## Setup Instructions

1. **Install the required library:**
   ```bash
   pip install inference-sdk
   ```

2. **Set up your environment variables:**
   - Copy the `.env.example` file and rename it to `.env`.
   - Paste your private Roboflow API key into the file.

3. **Run the script:**
   - Replace `"YOUR_IMAGE.jpg"` in `detect_trash.py` with the path to a real photo.
   - Run the script in your terminal:
     ```bash
     python detect_trash.py
     ```
