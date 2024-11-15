from ultralytics import YOLO

class ModelYOLO:
    def __init__(self) -> None:
        self.yolo = YOLO('yolov8n.pt')

    def predizer_frame(self, frame):
        return self.yolo.predict(frame)