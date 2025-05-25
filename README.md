# YOLOv11n-Based Drowsiness Detection

This project uses **YOLOv11n**, a lightweight and fast object detection model from [Ultralytics](https://github.com/ultralytics/ultralytics), to detect signs of **driver drowsiness** in real time. The model is trained on a labeled dataset from **Roboflow** and leverages heavy augmentations to improve generalization.

---

## 🚀 Features

- ✅ Trained on annotated eye/yawn images from Roboflow
- 🎛️ YOLOv11n model with strong data augmentations
- 🧪 Supports training, evaluation, and webcam-based inference
- 💾 Saves checkpoints to Google Drive for persistence
- ⚡ Optimized using the `AdamW` optimizer with early stopping

---

## 🧠 Dataset

Dataset is hosted and downloaded via **Roboflow**.

- Project: `Drosiness-Detection-3`
- Format: YOLOv8-compatible
- Includes: `train`, `val`, `test` images with bounding boxes

---

## Install Dependencies
 Make sure you have Python 3.8+ installed
``` pip install -r requirements.txt ```

---

## 🚀 How to Run the Project

### 🔧 Clone the repository
- ``` git clone(https://github.com/aditiprasadrao/drowsiness-detection-ml-miniproject.git) ```

- ``` cd Drowsiness-Detection-YOLOv11n ```

---
## Run Detection Script

``` python main.py ```
This will:
- Load best.pt (YOLOv11n model)
- Open your webcam
- Display real-time bounding boxes if drowsiness is detected
- Press Q to quit the webcam window.

---

## 🗂️ Folder Structure
Drowsiness-Detection-YOLOv11n/
├── best.pt # ✅ Pre-trained model weights (YOLOv11n)
├── main.py # ✅ Run this to start real-time detection
├── requirements.txt # Python dependencies
├── README.md # ✅ This file
├── drowsiness_yolo11_training.ipynb # 🧪 Jupyter notebook for training (optional)
├── Drosiness-Detection-3/ # (Optional) Dataset directory
│ ├── data.yaml
│ ├── train/
│ ├── val/
│ └── test/

---

📜 License
This project is licensed under the MIT License — free to use, distribute, and modify with attribution.

---
