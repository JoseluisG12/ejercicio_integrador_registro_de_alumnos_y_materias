class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,


                        }
    def run(self,Alu,Mat):
        band = True
        while band == True:
            b = int(input("""
    Menu Principal:
1- saber el promedio de un estudiante con o sin aplazo
2- saber segun el nombre de una materia que alumno la promociono con nomas mayor a 7
3- ver una lista de alumnos odenada por año que cursa de menor a mayor y ordenada alfabeticamente por apellido
0-salir\n"""))
            func = self.__switcher.get(b)
            if func:
                func(Alu,Mat)
            else:

                band = False

    def opcion1(self,Alu,Mat):
        dni = int(input("ingrese el dni del alumno a conocer su promedio\n"))
        alumno = Alu.buscarAlu(dni)
        sin_aplazo = Mat.promedioSA(alumno.getdni())
        con_aplazo = Mat.promedioCA(alumno.getdni())
        print("""
Alumno/a:{}
promedio sin aplazo:{}
promedio con aplazo:{:.2}""".format(alumno.getnombre(),sin_aplazo,con_aplazo))



    def opcion2(self,Alu,Mat):
        nomMat = input("ingrese el nombre de la materia\n")
        mateA = Mat.buscarMat(nomMat)
        if len(mateA) > 0:
            print("""
  DNI                Apellido y nombre                   Fecha         Nota      Año que cursa""")
            for materias_apro in mateA:
                alumno = Alu.buscarAlu(materias_apro.getdniM())
                print("""
{}               {} {}               {}         {}             {}""".format(alumno.getdni(),alumno.getapellido(),alumno.getnombre(),materias_apro.getfecha(),materias_apro.getnotaM(),alumno.getaño()))
        else:
            print("no se encontraron alumnos promocionales con nota mayor igual a 7")
    def opcion3(self,Alu,Mat):
        Alu.listaordena()



