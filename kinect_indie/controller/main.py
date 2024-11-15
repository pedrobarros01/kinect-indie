import cv2 as cv
from ..model.CameraControl import CameraControl
from ..model.YOLO import ModelYOLO
def run():
    camera_control = CameraControl(0, ModelYOLO())
    camera_control.ligar_camera()