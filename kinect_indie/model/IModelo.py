from abc import ABC, abstractmethod
import numpy as np
class IModelo(ABC):
    @abstractmethod
    def predizer_frame(self, frame):
        pass