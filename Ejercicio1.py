class Alumno:
    def __init__(self,nombre,apellido,edad,curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
    
    def programar(self):
        print(f"El alumno {self.nombre.upper()} {self.apellido.upper()} esta programado.")

alumno1 = Alumno("Nicolas","Stasyszyn",17,6)

alumno1.programar()
