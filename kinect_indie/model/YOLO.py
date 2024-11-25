from ultralytics import YOLO
from .IModelo import IModelo
class ModelYOLO(IModelo):
    def __init__(self) -> None:
        self.yolo = YOLO('yolov8n.pt')

    def predizer_frame(self, frame):
        return self.yolo.predict(frame)