from ultralytics import YOLO
import cv2

model = YOLO("../YOLO_weights/yolov8n.pt")

results = model("bus.jpg",show=True)
cv2.waitKey(0)

