import cv2 as cv
from ..model.CameraControl import CameraControl
def run():
    camera_control = CameraControl(0)
    camera_control.ligar_camera()