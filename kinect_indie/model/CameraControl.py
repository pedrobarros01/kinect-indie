import cv2 as cv

class CameraControl:
    def __init__(self, camera_id, exit_key='q') -> None:
        self.camera_id = camera_id
        self.exit_key = exit_key

    def ligar_camera(self):
        camera = cv.VideoCapture(self.camera_id)
        ligado = True
        while ligado:
            status, frame = camera.read()
            if not status or cv.waitKey(1) & 0xFF == ord(self.exit_key):
                ligado = False
            cv.imshow("Camera", frame)