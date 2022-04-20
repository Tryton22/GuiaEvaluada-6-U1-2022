
class Estudiantes(): #Clase con los nombres de los estudiantes que los ordena alfabeticamente.
    def __init__(self):
        self._alumnos = self.ordenar()

    def ordenar(self):
        self._alumnos = ["Alicia", "Marit", "Pepito", "David", "Eva", "Lucia",
                         "Rocio", "Andres", "Jose", "Belen", "Sergio", "Larry"]
        self._alumnos.sort()

        return self._alumnos