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

If you're downloading it using Roboflow in Colab:



