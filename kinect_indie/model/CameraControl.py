import cv2 as cv
from ..model.IModelo import IModelo
class CameraControl:
    def __init__(self, camera_id, modelo: IModelo, exit_key='q') -> None:
        self.camera_id = camera_id
        self.exit_key = exit_key
        self.modelo = modelo

    def ligar_camera(self):
        camera = cv.VideoCapture(self.camera_id)
        ligado = True
        while ligado:
            status, frame = camera.read()
            if not status or cv.waitKey(1) & 0xFF == ord(self.exit_key):
                ligado = False
            detection_results = self.modelo.predizer_frame(frame)
            for detection in detection_results:
                bounding_boxes = detection.boxes.xyxy
                for box in bounding_boxes:
                    x_min, y_min, x_max, y_max = map(int, box[:4])
                    if len(box) > 5:
                        class_id = int(box[5])
                        class_label = detection.names[class_id]
                        cv.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
                        cv.putText(frame, class_label, (x_min, y_min - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    else:
                        cv.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
            cv.imshow("Camera", frame)