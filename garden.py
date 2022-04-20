import random
from plantas import Plant

class Garden(Plant): #Clase que separa a cada estudiante con sus plantas al azar.
    def __init__(self):
        super().__init__()
        self._alicia = [Plant()._juntar[0][0], random.sample(Plant()._juntar[1], 4)]
        self._andres = [Plant()._juntar[0][1], random.sample(Plant()._juntar[1], 4)]
        self._belen = [Plant()._juntar[0][2], random.sample(Plant()._juntar[1], 4)]
        self._david = [Plant()._juntar[0][3], random.sample(Plant()._juntar[1], 4)]
        self._eva = [Plant()._juntar[0][4], random.sample(Plant()._juntar[1], 4)]
        self._jose = [Plant()._juntar[0][5], random.sample(Plant()._juntar[1], 4)]
        self._larry = [Plant()._juntar[0][6], random.sample(Plant()._juntar[1], 4)]
        self._lucia = [Plant()._juntar[0][7], random.sample(Plant()._juntar[1], 4)]
        self._marit = [Plant()._juntar[0][8], random.sample(Plant()._juntar[1], 4)]
        self._pepito = [Plant()._juntar[0][9], random.sample(Plant()._juntar[1], 4)]
        self._rocio = [Plant()._juntar[0][10], random.sample(Plant()._juntar[1], 4)]
        self._sergio = [Plant()._juntar[0][11], random.sample(Plant()._juntar[1], 4)]