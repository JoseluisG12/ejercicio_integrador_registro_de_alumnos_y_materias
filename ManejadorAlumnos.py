import numpy as np
from ClaseAlumnos import Alumnos
class RegistroAlumnos:
    __alumnos = []

    def __init__(self):
        self.__alumnos = []

    def mostraralumnos(self):
        print(len(self.__alumnos))
        for i in range(len(self.__alumnos)):
            self.__alumnos[i].mostrardatos()

    def cargardatosalumnos(self):
        dtype_alumno = np.dtype([('dni', int), ('apellido', 'U50'), ('nombre', 'U50'), ('carrera', 'U50'),('año', int)])  # Define la estructura de datos de los alumnos
        alumnos_arr = np.genfromtxt('alumnos.csv', delimiter=';', dtype=dtype_alumno,skip_header=1)  # Lee el archivo csv de alumnos y crea un arreglo NumPy con los datos
        for alumno_data in alumnos_arr:  # Crea un objeto Alumno para cada alumno y lo agrega al Manejador de Alumnos
            alumno = Alumnos(alumno_data['dni'], alumno_data['apellido'], alumno_data['nombre'], alumno_data['carrera'],alumno_data['año'])
            self.__alumnos.append(alumno)

    def buscarAlu(self,dni):

        band = False
        i = 0
        while band != True:
            if self.__alumnos[i].getdni() == dni:
                band = True
            else:
                i += 1
        return self.__alumnos[i]

    def listaordena(self):
        self.__alumnos.sort(reverse=True)
        años = [alumno.getaño() for alumno in self.__alumnos]
        años.sort()
        for i in range(len(años)):
            if i < len(años) - 1 and años[i] != años[i + 1]:
                print("""
AÑO {}""".format(años[i]))
                for alum in self.__alumnos:
                    if años[i] == alum.getaño():
                        print("""
{} {}""".format(alum.getapellido(),alum.getnombre()))
            elif i < len(años) - 1 and años[i] < años[i + 1]:#años[i] < años[i +1]-1
                print("""
AÑO {}""".format(años[i+1]))
                for alum in self.__alumnos:
                    if años[i] == alum.getaño():
                        print("""
                :{} {}""".format(alum.getapellido(), alum.getnombre()))











