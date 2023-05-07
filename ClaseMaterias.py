class Materias:
    __dni = ''
    __nombre = ''
    __fecha = ''
    __nota = ''
    __aprobacion = ''

    def __init__(self,dni,nombre,fecha,nota,apro):
        self.__dni = int(dni)
        self.__nombre = str(nombre)
        self.__fecha = str(fecha)
        self.__nota = int(nota)
        self.__aprobacion = str(apro)

    def mostrardatosM(self):
        print("""
    Materias:
DNI:{}
Nombre:{}
Fecha:{}
Nota:{}
Aprobacion:{}""".format(self.__dni,self.__nombre,self.__fecha,self.__nota,self.__aprobacion))

    def getdniM(self):
        return self.__dni

    def getnombreM(self):
        return self.__nombre

    def getnotaM(self):
        return self.__nota

    def getapro(self):
        return self.__aprobacion

    def getfecha(self):
        return self.__fecha

