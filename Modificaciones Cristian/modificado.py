class Persona:
    def __init__(self,id,nombre,contraseña,fechaNacimiento,correo,direccion,edad,genero,telefono,tipo_usuario,padecimiento):
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
        self.padecimiento=padecimiento
    def __str__(self):
        return ("Cedula = {}\n Nombre = {}\n contraseña = {}\n Fecha Nacimiento = {}\n "
                "Correo = {}\n Direccion = {}\n edad = {}\n genero = {}\n telefono = {}\n Tipo de usuario = {}\n padecimiento = {}".format(self.id,self.nombre,self.contraseña,
                                                              self.fechaNacimiento,self.correo,self.direccion,self.edad,self.genero,self.telefono,self.tipo_usuario,self.padecimiento))
class Citas:
    def __init__(self,id,paciente,fecha,hora,padecimiento,doctor):
        self.id=id
        self.paciente=paciente
        self.fecha=fecha
        self.hora=hora
        self.padecimiento=padecimiento
        self.doctor=doctor
    def __str__(self):
        return ("Cedula = {}\n paciente = {}\n fecha = {}\n hora = {}\n "
                "padecimiento = {}\n doctor = {}".format(self.id,self.paciente,self.fecha,
                                                              self.hora,self.padecimiento,self.doctor))
class Recetas:
    def __init__(self,id,nombreMedi,formaMedi,cantiDias):
        self.id=id
        self.nombreMedi=nombreMedi
        self.formaMedi=formaMedi
        self.cantiDias=cantiDias

    def __str__(self):
            return ("Cedula: {}\n Medicamento : {}\n Forma de tomar el medicamento= {}\n Cantidad de Dias = {}\n "
                    .format(self.id,self.nombreMedi, self.formaMedi,self.cantiDias))
class AtencionPaciente:
    def __init__(self,id,fecha,nombre,sintomas,nivelDolor,posicion,diagnostico,doctor,receta):
        self.id=id
        self.fecha=fecha
        self.nombre=nombre
        self.sintomas=sintomas
        self.nivelDolor=nivelDolor
        self.posicion=posicion
        self.diagnostico=diagnostico
        self.doctor=doctor
        self.receta=receta

    def __str__(self):
            return ("Cedula: {}\nfecha:{}\n Nombre : {}\n Sintomas:{}\n Nivel de dolor : {}\n posicion : {}\nDiagnostico:{}\nDoctor:{}\n Receta{}"
                    .format(self.id,self.fecha,self.nombre, self.sintomas,self.nivelDolor,self.posicion,self.diagnostico,self.doctor,self.receta))


listaAtenderPacientes=[]
listaRecetas=[]
listaPersonas=[]
listaCitas = []
cristian = Persona (123,"cris","123","1995/04/05","andre@gmail.com","Barrio los Angeles",24,"M","2460-54-51","medico","No tengo")
listaPersonas.append(cristian)
gloria = Persona (123,"gloria","123","1995/04/05","gloria@gmail.com","Barrio los Angeles",24,"M","2460-54-51","secretaria","No tengo")
listaPersonas.append(gloria)
maria = Persona (321,"maria","321","1998/04/19","chamo@gmail.com","Cedral",19,"M","2460-29-11","secretaria","No tengo")
listaPersonas.append(maria)
eduardo =Citas(456,"eduardo","08/14/17","9:00 pm","Dolor de cabeza",cristian.nombre)
listaCitas.append(eduardo)

lionel=AtencionPaciente(eduardo.id,eduardo.fecha,eduardo.paciente,"Dolor de Rodilla","8","pie izquierdo","ligamento cruzado reventado",cristian.nombre,"hierro")
listaAtenderPacientes.append(lionel)

def menuInicio(listaPersonas,listaCitas):
    while True:
        try:
            print("\n1-Iniciar sesion\n"
                  "2-Registrarse\n"
                  "3-Salir\n")
            opMenuIni = int(input("Seleccione una opcion:"))
            if opMenuIni == 1:
                iniciarSeccion(listaPersonas,listaCitas)

            elif opMenuIni== 2:
                registro(listaPersonas)

            elif opMenuIni == 3:
                print("\nGracias por preferirnos\n")
                break
        except ValueError:
            print("Me cago en TODO lo que se menea\nNO DEBES PONER LETRAS NI MUCHOS NUMEROS A LA VEZ\nSTEEE MENNNN  :V")

# 1.

def iniciarSeccion(lista,listaCitas):
   while True:
        valorI = 0
        valorC = 0
        valorT = 0
        while True:
            try:
                cedula = int(input("Digite su número de cedula: "))
                break
            except ValueError:
                print("MAMON!\nNO PONGAS LETRAS EN LA CEDULA!!!\n")
        while True:
            try:
                contraseña = str(input("Digite su contraseña: "))
                if contraseña.isalnum():
                    break
                else:
                    print("      ¡Error!\nSolo puedes usar numeros y letras\n")
            except:
                print("no no ")
        for i in lista:
            if i.id == cedula:
                valorI = True
                if i.contraseña == contraseña:
                    valorC = True
                    if i.tipo_usuario == "medico":
                        valorT = True
                        break
                    elif i.tipo_usuario == "secretaria":
                        valorT = False
                        break

                elif i.contraseña != contraseña:
                    valorC = False
                elif i.contraseña==contraseña:
                    valorC = False
                elif i.id != cedula:
                    valorI = False



        if valorI == True and valorC == True and valorT == True:
            print("Cedula y Contraseña correctas\n")
            print("Bienvenido Medico\n")
            menuPrincipalMedicos(listaPersonas)

        elif valorI == True and valorC == True and valorT == False:
            print("\nCedula y Contraseña correctas")
            print("\nBienvenido Secretaria\n")
            menuPrincipalSecretaria(listaPersonas,listaCitas)

        elif valorI == False and valorC == True:
            print("\nCedula o contraseña invalida")
        elif valorI == True and valorC == False:
            print("\nCedula o contraseña invalida")
        elif valorI == False and valorC == False:
            print("\nCedula o contraseña invalida")

        # 1.1
#arreglar validaciones

def menuPrincipalMedicos (listaPersonas):#1.1.1

    print("1-Consultar citas\n"
                "2-Registrar cita\n"
                "3-Atender Pacientes\n"
                "4-Recetas\n"
                 "5-Salir\n")



    opMedico=input("Seleccione  una opcion : " )
    if opMedico == "1":
        ConsultarCita()

    elif opMedico == "2":
        registrarCita(listaPersonas,listaCitas)
    elif opMedico =="3":
        id = str(input("Digite la cedula:"))
        atenderPaciente(listaAtenderPacientes,listaCitas)
    elif opMedico =="4":
       insertarReceta(listaRecetas)
    elif opMedico =="5":
        print("Gracias por preferirnos")

        menuInicio(listaPersonas,listaCitas)


                # 1.1.1
#Aqui van Def de Menu principal medicos

def ConsultarCita():
    print("Menu\n"
          "Seleccione una opcion :\n"
          "1-Citas del dia\n"
          "2-Fecha expecifica\n"
          "3-Salir")
    opCita=int(input("Seleccione una opcion: "))

    if opCita==1:
        citasDia()
    elif opCita==2:
        fecha=str(input("Digite la fecha:"))
        fechaEspecifica(fecha)
    elif opCita==3:
        print ("Gracias por preferirnos\n")
        menuPrincipalMedicos(listaPersonas)


#Menu Consultar Citas
import time
def citasDia():#Colocar bien el formato de la fecha.
    result=""
    for x in listaCitas:
        if x.fecha==time.strftime("%x"):
            result += x.id + " " + x.paciente + " " + x.hora
            result += "\n"
            print("Cedula:{}\nPaciente:{}\nHora:{}".format(x.id, x.paciente, x.hora))
        elif x.fecha!=time.strftime("&x"):
            print("No tiene citas ")

#Menu Consultar Citas

def fechaEspecifica(fecha):
    result = ""
    for x in listaCitas:
        if x.fecha == fecha:
            result += x.id + " " + x.paciente + " " + x.hora
            result += "\n"
            print ("Cedula:{}\nPaciente:{}\nHora:{}".format(x.id,x.paciente,x.hora))
        elif x .fecha!=fecha:
            print("No tiene Citas esta fecha")


#Funciones de la opcion Receta
def receta(listaAtenderPacientes,id):
    for r in listaAtenderPacientes:
        if r.id  ==r.id:
            id=str(input("Digete la cedula del paciente: "))
            receta(listaAtenderPacientes,id)

def insertarReceta(listaRecetas):
    id=str(input("Digite la cedula:"))
    nombreMedi=str(input("Digite el nombre del medicamento:"))
    formaMedi=str(input("Digite la forma de tomar el medicamento"))# Recomendacion
    cantiDias=str(input("Digite la cantidad de dias:"))
    registroRecetas=Recetas(id,nombreMedi,formaMedi,cantiDias)
    listaRecetas.append(registroRecetas)

#funciones de la opcion Atender pacientes
def insertarAtenderPacientes(listaAtenderPacientes): #Faltaria la manera de validar cedula con citas y citas de secretaria
    cedula = str(input("Digite la cedula:"))
    fecha=str(input("Digete la fecha:"))
    sintomas=str(input("Digete los sintomas: "))
    nivelDolor=str(input("Digete el nivel de dolor:"))#Rango de dolor
    posicion=str(input("Digete la posicion:"))#Area
    diagnostico=str(input("Digete el diagnostico:"))
    doctor=str(input("Digete el doctor"))
    receta=str(input("Digete la receta"))
    registroAtencionPaciente=AtencionPaciente(cedula,fecha,"",sintomas,nivelDolor,posicion,diagnostico,doctor,receta)
    listaAtenderPacientes.append(registroAtencionPaciente)


def atenderPaciente(listaAtenderPacientes,listaCitas,):
    import time
    for x in listaAtenderPacientes:
        if x.id==id:
            insertarAtenderPacientes(listaAtenderPacientes,)
            for c in listaCitas:
             if c.id!=c.id:
                 print ("No esta registrado en la cita,")
             elif  time.strftime("%I:%M:%S")==c.hora and c.hora >1:
                 print ("Registrarse en la cita para poder ser Atendido por el doctor")


def menuPrincipalSecretaria(listaPersonas,listaCitas):

   print("\n1-Registrar cita\n"
                   "2-Imprimir comprobante\n"
                   "3-Registrar paciente \n"
                   "4-Salir\n ")


   opSecretaria=input("Seleccione una opcion: ")

   if opSecretaria == "1":
       registrarCita(listaPersonas,listaCitas)

   elif opSecretaria == "2":
       ImprimirComprobante(listaAtenderPacientes)

   elif opSecretaria == "3":
       registrarPaciente(listaPersonas)
   elif opSecretaria == "4":
       print("Gracias por preferirnos")
       menuInicio(listaPersonas,listaCitas)

#Pacientes
def iniciar_seccion_paciente(listaPersonas):
    for x in listaPersonas:
        if x.id=="paciente":
            cedula=str(input("Digete la cedula:"))
            menuPrincipalPaciente(listaPersonas)


def citasPendientes(listaCitas):
    result = ""
    for x in listaCitas:
        if x.fecha < time.strftime("%x"):
            result += x.fecha + " " + x.hora + " "
            result += "\n"
            print("Fecha:{}\nHora:{}".format(x.fecha ,x.hora))

def menuPrincipalPaciente(ListaPersonas):

                print("1-Ultimas 3 recetas\n"
                      "2-Expediente Medico\n"
                      "3-Citas pendientes\n"
                      "4-Salir\n")

                opPaciente = int(input("Digete una opción: "))

                if opPaciente == 1:
                    menuPrincipalPaciente(listaPersonas)

                elif opPaciente == 2:
                    pass

                elif opPaciente == 3:
                    citasPendientes(listaCitas)
                elif opPaciente == 4:
                    print ("Gracias por escogernos:")
                    menuInicio(listaPersonas, listaCitas)








                    #1.1.2
#opciones menu secretaria
def registrarCita(listaPersonas,listaCitas):
    while True:
        id = str(input("Digite la cedula :"))
        paciente = str(input("Digete el nombre del paciente :"))
        fecha = str(input("Digete la fecha :"))
        hora = str(input("Digete la hora :"))
        padecimiento = (input("Digete el padecimiento : "))
        doctor = input("Digete el nombre del doctor: ")
        registroCitas = Citas(id, paciente, fecha, hora, padecimiento, doctor)
        listaCitas.append(registroCitas)
        print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\npadecimiento:{}\ndoctor:{}".format(id, paciente, fecha, hora,
                                                                                              padecimiento, doctor))
        op = input("Desea registrar otra cita s/n ")
        if op == "s":
            pass
        elif op == "n":
            menuPrincipalSecretaria(listaPersonas, listaCitas)
            break
        else:
            print("Valor invalido")

                        #1.1.2.1

def ImprimirComprobante(listaAtenderPacientes):
    cedula=str(input("Digete la cedula del paciente: "))
    fecha=str(input("Digete la fecha de la cita: "))
    for x in listaAtenderPacientes:
        if x.id== cedula and x.fecha ==fecha:
            print ("Nombre del paciente: {}\nConsultorio medico: Digitaldoctor\n"
                   "Medico: {}\nFecha: {}\nDiagnostico: {}"
                   .format(x.nombre,x.doctor,x.fecha,x.diagnostico))
            menuPrincipalSecretaria(listaPersonas,listaCitas)
            break

        elif x.id !=cedula and x.fecha!=fecha:
            print ("Cedula o fecha invalida")

        elif x.id ==cedula and x.fecha !=fecha:
            print ("Cedula o fecha invalida")

        elif x.id !=cedula and x.fecha == fecha:
            print ("Cedula o fecha invalida")





                   #1.1.2.2

def registrarPaciente(listaPersonas):
    existe = ""
    existe2 = ""
    doc = ""
    nombre = ""
    while True:
        while True:
            try:
                cedula = str(input("Digite su número de cedula: "))
                if len(cedula) == 9:
                    for i in listaPersonas:
                        if i.id == id:
                            existe = True
                            nombre = i.nombre
                            break
                        elif i.id != id:
                            existe = False
                    print(nombre)
                break
            except ValueError:
                print("MAMON!\nNO PONGAS LETRAS EN LA CEDULA!!!\n")

            fecha = str(input("Digete la fecha :"))
            hora = str(input("Digete la hora :"))
            print("Doctores:")
            for t in listaPersonas:
                if t.tipo_usuario == "Medico":  # Revisar este proceso
                    print("Doctor:", t.nombre)
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

                        #1.1.2.3

def registro(listaPersonas):
    id = str(input("Digite la cedula: "))
    contraseña = str(input("Digite la contraseña: "))
    nombre =str (input("Digite el nombre: "))
    fechaNacimiento = str(input("Digete  la fecha de nacimiento: "))
    correo = str(input("Digete el correo: "))
    direccion = str(input("Digite la dirección: "))
    edad = int(input("Digite la edad:"))
    genero = str(input("Digite el genero: "))
    telefono = str(input("Digite el telefono : "))
    tipoUsuario = str(input("Digete el tipo de usuario : "))
    padecimiento=str(input("Digete si tiene algun padecimiento:"))
    objregistro = Persona(id,nombre,contraseña,fechaNacimiento,correo,direccion,edad,genero,telefono,tipoUsuario,padecimiento)
    listaPersonas.append(objregistro)

    menuInicio(listaPersonas,listaCitas)

        #1.2
#Registro




# Programa Principal:

print(time.strftime("%x"))
menuInicio(listaPersonas,listaCitas)

#time.strftime("%I:%M:%S")#hora



