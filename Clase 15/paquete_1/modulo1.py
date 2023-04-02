class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota del alumno:", self.nota)