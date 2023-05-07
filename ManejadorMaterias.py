from ClaseMaterias import Materias
import csv
class MateriasA:
    __Materiasapro = []

    def __init__(self):
        self.__Materiasapro = []


    def mostrarmaterias(self):
        for i in range(len(self.__Materiasapro)):
            self.__Materiasapro[i].mostrardatosM()

    def cargardatosMat(self):
        lista = []
        archivo = open('materiasAprobadas.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)  # salta la primera fila que son los encabezados
        for fila in reader:
            lista.append(fila)
        for mat in lista:
            materia = Materias(mat[0], mat[1], mat[2], mat[3], mat[4])
            self.__Materiasapro.append(materia)

    def promedioSA(self,dni):
        acumM = 0
        contM = 0
        for i in range(len(self.__Materiasapro)):
            if self.__Materiasapro[i].getdniM() == dni and self.__Materiasapro[i].getnotaM() > 6:
                acumM += self.__Materiasapro[i].getnotaM()
                contM += 1
        if contM == 0:
            contM = 1
            return (acumM / contM)
        else:
            return (acumM / contM)

    def promedioCA(self,dni):
        acumM = 0
        contM = 0
        for i in range(len(self.__Materiasapro)):
            if self.__Materiasapro[i].getdniM() == dni:
                acumM += self.__Materiasapro[i].getnotaM()
                contM += 1

        if contM == 0:
            contM = 1
            return (acumM / contM)
        else:
            return (acumM / contM)

    def buscarMat(self,nom):
        listaMA = []
        for materiaA in self.__Materiasapro:
            if materiaA.getnombreM() == nom and materiaA.getnotaM() >= 7 and materiaA.getapro() == 'P':
                listaMA.append(materiaA)
        return listaMA





