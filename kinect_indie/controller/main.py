import cv2 as cv
from ..model.camera_control import CameraControl
from ..model.YOLO import ModelYOLO
from ..services.front_app import coletar_teclas

def run():
    teclas = coletar_teclas()

    if teclas:
        exit_key, left_key, right_key, jump_key = teclas
        camera_control = CameraControl(0, ModelYOLO(), (640, 480), exit_key, left_key, right_key, jump_key)
        camera_control.ligar_camera()
    else:
        print('Nenhuma tecla foi inserida')
        camera_control = CameraControl(0, ModelYOLO(), (640, 480), 'q', 'left', 'right', 'space')
        camera_control.ligar_camera()