#Menu y funciones del medico(consultar, registrar, atender, receta
#Menu y funciones de secretaria (Imprimir comprobante)
#Menu de consulta de los paciente
#Revisar los While True de los registros
#Preguntar para ver si se puede hacer con While True Try/except
#Ayuda con clases
#Validar una fecha
#Validar cedula en lista y que imprima el nombre de la cedula en registrar cita
#Verifique correo
#Verifique numero de telefono de 8 digitos no importa si esta dividido por un "-"
#Preguntar sobre puntaje del proyecto para evitar tantas validaciones que nos estan atrasando
# registrar citas y que no tenga mas de 2 citas por semana.


class Persona:
    def __init__(self,id,nombre,contraseña,fechaNacimiento,correo,
                 direccion,edad,genero,telefono,tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.fechaNacimiento = fechaNacimiento
        self.correo = correo
        self.direccion = direccion
        self.edad = edad
        self.genero = genero
        self.telefono = telefono
        self.tipo_usuario =tipo_usuario

    def __str__(self):
        return ("Cedula = {}\n Nombre = {}\n contraseña = {}\n Fecha Nacimiento = {}\n "
                "Correo = {}\n Direccion = {}\n edad = {}\n genero = {}\n telefono = {}"
                "\n Tipo de usuario = {}"
                .format(self.id,self.nombre,self.contraseña,self.fechaNacimiento,self.correo,
                self.direccion,self.edad,self.genero,self.telefono,self.tipo_usuario))

class funcionarios(Persona):
    pass

class pacientes(Persona):
    tipoSangre = ""

class Citas:
    def __init__(self,id,paciente,fecha,hora,doctor):
        self.id=id
        self.paciente=paciente
        self.fecha=fecha
        self.hora=hora
        self.doctor=doctor

    def __str__(self):
        return ("Cedula = {}\n paciente = {}\n fecha = {}\n hora = {}"
                "\n doctor = {}".format(self.id,self.paciente,
                                        self.fecha,self.hora,self.doctor))

listaPersonas=[]
listaCitas = []
#Medicos
medico1 = Persona ("207790516","Cristian","crisov1998","19/05/1998",
                   "cristianov19@gmail.com","Cedral",19,"Masculino","8521-3563","Medico",)
listaPersonas.append(medico1)
medico2 = Persona("987","Alfonso","987","26/02/1998","dacripo98@gmail.com","Barrio Lourdes",
                  25,"Masculino","8879-4982","Medico")
listaPersonas.append(medico2)
#Secretarias
secretaria1= Persona ("321","Maria","321","6-05-98","ermelindasilvaramirez@gmail.com",
                      "Cedral",19,"M","6061-5729","Secretaria")
listaPersonas.append(secretaria1)

#Pacientes
paciente1 = Persona("209990521","Eduardo","123","13/03/1972","eduguzmanvindas@gmail.com",
                    "Barrio los Angeles",23,"Masculino","8707-3663","Paciente")
listaPersonas.append(paciente1)

#Citas
eduardo = Citas(paciente1.id,paciente1.nombre,"04/05/2018","4:00 pm",medico1.nombre)
listaCitas.append(eduardo)

def menuInicio(listaPersonas,listaCitas):
    while True:
        print("\n1-Iniciar sesion\n"
          "2-Registrarse\n"
          "3-Salir\n")
        opMenuIni = int(input("Seleccione una opcion:"))
        try:
            if opMenuIni == 1:
                iniciarSeccion(listaPersonas,listaCitas)

            elif opMenuIni == 2:
                registro(listaPersonas)

            elif opMenuIni == 3:
                print("\nGracias por preferirnos\n")
                break
        except ValueError:
            print("Me cago en TODO lo que se menea")

# 1.

def iniciarSeccion(lista,listaCitas):
   while True: #Arreglar cuando las contraseña y cedula estan en lista, pero no son la misma persona
        valorI = ""
        valorC = ""
        valorT = ""
        cedula = str(input("Digite su número de cedula: "))
        contraseña = str(input("Digite su contraseña: "))
        for i in lista:
            if i.id == cedula:
                valorI = True
                if i.contraseña == contraseña:
                    valorC = True
                    if i.tipo_usuario == "Medico":
                        valorT = True
                        break
                    elif i.tipo_usuario == "Secretaria":
                        valorT = False
                        break
                    else:
                        print("No eres Doctor ni secretaria, debes ser paciente")

                elif i.contraseña != contraseña:
                    valorC = False
            elif i.id != cedula:
                valorI = False

        if valorI == True and valorC == True and valorT == True:
            print("\nCedula y Contraseña correctas")
            print("\nBienvenido Medico\n")
            menuPrincipalMedicos(listaPersonas)


        elif valorI == True and valorC == True and valorT == False:
            print("\nCedula y Contraseña correctas")
            print("\nBienvenido Secretaria\n")
            menuPrincipalSecretaria(listaPersonas,listaCitas)
            break

        elif valorI == False and valorC == True:
            print("\nCedula o contraseña invalida")
        elif valorI == True and valorC == False:
            print("\nCedula o contraseña invalida")
        elif valorI == False and valorC == False:
            print("\nCedula y contraseña invalida")

        # 1.1
#arreglar validaciones

def menuPrincipalMedicos (listaPersonas):#1.1.1

    print("\n1-Consultar citas\n"
                "2-Registrar cita\n"
                "3-Atender Pacientes\n"
                "4-Recetas\n"
                 "5-Salir\n")



    opMedico=input("Seleccione  una opcion : " )
    if opMedico == "1":
        pass
    elif opMedico == "2":
        pass
    elif opMedico =="3":
        pass
    elif opMedico =="4":
        pass
    elif opMedico =="5":
        print("Gracias por preferirnos")
        menuInicio(listaPersonas,listaCitas)

                # 1.1.1
#Aqui van Def de Menu principal medicos



def menuPrincipalSecretaria(listaPersonas,listaCitas):

   print("\n1-Registrar cita\n"
                   "2-Imprimir comprobante\n"
                   "3-Registrar paciente \n"
                   "4-Salir\n ")


   opSecretaria=input("Seleccione una opcion: ")

   if opSecretaria == "1":
       registrarCita(listaPersonas,listaCitas)

   elif opSecretaria == "2":
       ImprimirComprobante(listaCitas)

   elif opSecretaria == "3":
       registrarPaciente(listaPersonas)
   elif opSecretaria == "4":
       print("Gracias por preferirnos")
       menuInicio(listaPersonas,listaCitas)

   def menuPrincipalPaciente():

       print("\nUltimas 3 recetas\n"
             "2-Expediente Medico\n"
             "3-Citas pendientes\n"
             "4-Salir\n")


       opPaciente = input("Seleccione  una opcion : ")
       if opPaciente == "1":
           pass

       elif opPaciente == "2":
           pass

       elif opPaciente == "3":
           pass

       elif opPaciente =="4":
           print("Gracias por preferirnos")
           menuInicio(listaPersonas,listaCitas)

                #1.1.2
#opciones menu secretaria

def registrarCita(listaPersonas, listaCitas):
    existe = ""
    existe2= ""
    doc = ""
    nombre = ""
    while True:
        id = str(input("Digite la cedula :"))
        if len(id) == 9 :
            for i in listaPersonas:
                if i.id == id:
                    existe = True
                    nombre = i.nombre
                    break
                elif i.id != id:
                    existe = False
            print(nombre)
            fecha = str(input("Digete la fecha :"))
            hora = str(input("Digete la hora :"))
            print("Doctores:")
            for t in listaPersonas:
                if t.tipo_usuario == "Medico":#Revisar este proceso
                    print("Doctor:", t.nombre)
                    doc = t.nombre
            doctor = input("Digete el nombre del doctor: ")
            for l in listaPersonas:
                if doctor == l.nombre:
                    existe2 = True
                    doctor = doc
                    break
                elif doctor != l.nombre:
                    existe2 = False
                else:
                    existe2 = False
            if existe2 == True:
                registroCitas = Citas(id, nombre, fecha, hora, doctor)
                listaCitas.append(registroCitas)
                print(listaCitas[-1])
                break
            elif existe2 == False:
                print("Valor invalido")
            else:
                print("Valor invalido")
        else:
            print("La cedula tiene que tener 9 digitos")


        #print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\ndoctor:{}"
        #       .format(id, paciente, fecha, hora,doctor))
        op = input("Desea registrar otra cita s/n ")
        if op == "s":
            pass
        elif op == "n":
            menuPrincipalSecretaria(listaPersonas, listaCitas)
            break
        else:
            print("Valor invalido")

                        #1.1.2.1

def ImprimirComprobante(listaCitas):
    pass

                        #1.1.2.2

def registrarPaciente(listaPersonas):# No Vuelve a pedir el mismo valor cuando es invalido
    while True:
        print("Registrar paciente: ")
        id = str(input("Digite la cedula del paciente: "))
        if len(id) == 9:
            for i in listaPersonas:
                if i.id == id:
                    print("Esa Cedula ya esta Registrada")
                    break
                elif i.id != id:
                    nombre = str(input("Digite el nombre del paciente: "))
                    fechaNacimiento = str(input("Digete  la fecha de nacimiento del paciente: "))
                    correo = str(input("Digete el correo del paciente: "))
                    direccion = str(input("Digite la dirección del paciente: "))
                    edad = int(input("Digite la edad del paciente:"))
                    if edad <=100:
                        genero = str(input("Digite el genero del paciente: "))
                        if genero == "Masculino" or genero == "Femenino":
                            telefono = str(input("Digite el telefono del paciente : "))
                            paciente = Persona(id,nombre,"",fechaNacimiento,
                                           correo,direccion,edad,genero,telefono,"Paciente")
                            listaPersonas.append(paciente)
                            op = input("Desea registrar otra cita s/n ")
                            if op == "s":
                                pass
                            elif op == "n":
                                menuPrincipalSecretaria(listaPersonas, listaCitas)
                                break
                            else:
                                print("Valor invalido")
                        else:
                            print("Valor invalido")
                    elif edad > 100:
                        print("Edad Invalida")
                    else:
                        print("Valor Invalido")
        elif len(id) != 9:
            print("La cedula tiene que tener 9 digitos\n\nNota: La cedula solo debe contener números.")
        else:
            print("Valor invalido\nDigite Enter para Continuar")
            input()


                        #1.1.2.3

def registro(listaPersonas):
    while True:
        id = str(input("Digite la cedula: "))
        if len(id) == 9:
            for i in listaPersonas:
                if i.id == id:
                    print("\nEsta cedula ya ha sido Registrada\n")
                    break
                if i.id != id:
                    contraseña = str(input("Cree una nueva contraseña: "))
                    nombre = str(input("Digite el nombre: "))
                    fechaNacimiento = str(input("Digete  la fecha de nacimiento: "))  # Valida fecha de nacimiento
                    correo = str(input("Digete el correo: "))  # Validar correo
                    direccion = str(input("Digite la dirección: "))
                    edad = int(input("Digite la edad:"))
                    if edad < 17 or edad <= 100  :
                        genero = str(input("Digite el genero: "))
                        if genero == "Masculino" or genero == "Femenino":
                            telefono = str(input("Digite el telefono : "))
                            tipoUsuario = str(input("Digete el tipo de usuario : "))
                            if  tipoUsuario == "Medico" or tipoUsuario == "Secretaria":
                                objregistro = Persona(id, nombre,contraseña, fechaNacimiento, correo, direccion, edad,
                                                      genero,telefono, tipoUsuario)
                                listaPersonas.append(objregistro)

                                op = input("Desea registrar otra cita s/n ")
                                if op == "s":
                                    pass
                                elif op == "n":
                                    menuInicio(listaPersonas, listaCitas)
                                    break
                                else:
                                    print("Valor invalido")
                            else:
                                print("el tipo de usuario solo puede ser 'Medico' o 'Secretaria'.")
                        else:
                            print("Valor invalido")
                    elif edad > 100 :
                        print("La edad no es valida")
                    else:
                        print("Valor invalido")
        elif len(id) != 9:
            print("La cedula tiene que tener 9 digitos\n\nNota: La cedula solo debe contener números.")
        else:
            print("Valor invalido\nDigite Enter para Continuar")
            input()



menuInicio(listaPersonas,listaCitas)