from estudiante import Estudiantes

class Plant(Estudiantes): #Clase para las plantas y para juntar el nombre de las plantas con los alumnos.
    def __init__(self):
        super().__init__()
        self._nombre_planta = ["Hierba", "Trébol", "Rábanos", "Violetas"]
        self._juntar = self.juntar_estudiante()


    def juntar_estudiante(self):
        l1 = self._nombre_planta
        l2 = self._alumnos
        self._juntar = [l2] + [l1]
        
        return self._juntar