from ultralytics import YOLO
import cv2
import os

model = YOLO(r"C:\Users\Advaita P Rao\Aditi docs\drowsiness_detection_ml_miniproj\yolo11_approach\drowsiness-detection-ml-miniproject\best.pt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Check if anything was detected
    if len(results[0].boxes) == 0:
        print("No detections")
    else:
        print(f"Detections: {len(results[0].boxes)}")

    try:
        # Try displaying with OpenCV
        cv2.imshow("YOLO Drowsiness Detection", annotated_frame)

        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    except cv2.error:
        print("cv2.imshow not supported. Saving frame instead.")
        os.makedirs("output_frames", exist_ok=True)
        cv2.imwrite(f"output_frames/frame_{frame_count}.jpg", annotated_frame)

        # Stop after saving a few frames
        frame_count += 1
        if frame_count > 5:
            print("Saved 5 frames. Exiting.")
            break

cap.release()
cv2.destroyAllWindows()
