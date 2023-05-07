from ManejadorAlumnos import RegistroAlumnos
from ManejadorMaterias import MateriasA
from ClaseMenu import Menu


if __name__=='__main__':
    manejadorAlu = RegistroAlumnos()
    manejadorAlu.cargardatosalumnos()
    manejadorMat = MateriasA()
    manejadorMat.cargardatosMat()
    menu = Menu()
    menu.run(manejadorAlu,manejadorMat)
