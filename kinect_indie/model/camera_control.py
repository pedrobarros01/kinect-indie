import cv2 as cv
from .IModelo import IModelo
from ..services.game_service import GameService
import pyautogui

pyautogui.FAILSAFE = False

class CameraControl:
    def __init__(self, camera_id, modelo: IModelo, resolution: tuple[int, int], exit_key, left_key, right_key, jump_key) -> None:
        self.camera_id = camera_id
        self.exit_key = exit_key
        self.left_key = left_key
        self.right_key = right_key
        self.jump_key = jump_key
        self.modelo = modelo
        self.resolution = resolution
        self.line_start = (0,50)
        self.line_end = (self.resolution[1] + 170, 50)
        self.quad_esq = [(25, 200), (75, 300)]
        self.quad_dir = [(550, 200), (600, 300)]
        self.line_color = (0,0,255)
        self.thickness = 2

    def ligar_camera(self):
        camera = cv.VideoCapture(self.camera_id)
        ligado = True
        while ligado:
            status, frame = camera.read()
            if not status or cv.waitKey(1) & 0xFF == ord(self.exit_key):
                ligado = False
            frame = cv.flip(frame, 1)
            detection_results = self.modelo.predizer_frame(frame)
            points_minimum_player = None
            points_maximum_player = None
            for detection in detection_results:
                bounding_boxes = detection.boxes.xyxy
                for box in bounding_boxes:
                    x_min, y_min, x_max, y_max = map(int, box[:4])
                    '''class_id = int(box[5])
                    class_label = detection.names[class_id]
                    if class_label == 'person':'''
                    cv.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
                    #cv.putText(frame, class_label, (x_min, y_min - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    points_minimum_player = (x_min, y_min)
                    points_maximum_player = (x_max, y_max)
            
            cv.line(frame, self.line_start, self.line_end, self.line_color, self.thickness)
            cv.rectangle(frame, (self.quad_esq[0][0], self.quad_esq[0][1]), (self.quad_esq[1][0], self.quad_esq[1][1],), (0,0,255), 2)
            cv.rectangle(frame, (self.quad_dir[0][0], self.quad_dir[0][1]), (self.quad_dir[1][0], self.quad_dir[1][1],), (0,0,255), 2)
            if points_minimum_player != None and points_minimum_player != None:
                if GameService.pulou(points_minimum_player, [self.line_start, self.line_end]):
                    pyautogui.press(self.jump_key)
                    print('\nPulou\n')
                elif GameService.mover(points_minimum_player, points_maximum_player, self.quad_esq):
                    pyautogui.press(self.left_key)
                    print(points_maximum_player)
                    print('\nMoveu pra esquerda\n')
                elif GameService.mover(points_minimum_player, points_maximum_player, self.quad_dir):
                    pyautogui.press(self.right_key)
                    print('\nMoveu pra direita\n')
            else:
                print('Nada')
           
            cv.imshow("Camera", frame)     