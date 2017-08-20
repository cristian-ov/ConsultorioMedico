class Persona:
    def __init__(self,id,nombre,contraseña,fechaNacimiento,correo,direccion,edad,genero,telefono,tipo_usuario):
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
                "Correo = {}\n Direccion = {}\n edad = {}\n genero = {}\n telefono = {}\n Tipo de usuario = {}".format(self.id,self.nombre,self.contraseña,
                                                              self.fechaNacimiento,self.correo,self.direccion,self.edad,self.genero,self.telefono,self.tipo_usuario))
class paciente:
    def __init__(self,id,nombre,fechaNacimiento,correo,direcion,edad,genero,
                 telefono,padecimiento,medico):
        self.id = id
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.padecimiento = padecimiento
        self.medico = medico
        self.cita= citas = []
        self.atencionpaciente = []
        self.recetas =[]
        
    def medicamento (self,receta):
        self.recetas.append(receta)

    def atender (self,atencion):
        self.atencionpaciente.append(atencion)

    def citaPac(self,cita):
        self.cita.append(cita)

    def __str__(self):
        #or i in
        return ("Cedula = {}\nNombre = {}\nFecha de Nacimiento = {}\n"
                "Padecimiento = {}\nMedico = {}\n{}\n{}\n{}".format(self.id,self.nombre,
                                                         self.fechaNacimiento,
                                                         self.padecimiento,self.medico,
                                                        self.cita,self.atencionpaciente,self.recetas))
class Citas:
    def __init__(self,fecha,hora,doctor):
        self.fecha=fecha
        self.hora=hora
        self.doctor=doctor

    def __str__(self):
        return ("\n fecha = {}\n hora = {}"
                "\n doctor = {}".format(self.fecha,self.hora,self.doctor))
class Receta:
    def __init__(self,nombreMedi,formaMedi,cantiDias):
        self.nombreMedi=nombreMedi
        self.formaMedi=formaMedi
        self.cantiDias=cantiDias

    def __str__(self):
            return ("\nMedicamento : {}\n Forma de tomar el medicamento= {}\n Cantidad de Dias = {}\n "
                    .format(self.nombreMedi, self.formaMedi,self.cantiDias))
class AtencionPaciente:
    def __init__(self,sintomas,nivelDolor,posicion,diagnostico,doctor,receta):
        self.sintomas=sintomas
        self.nivelDolor=nivelDolor
        self.posicion=posicion
        self.diagnostico=diagnostico
        self.doctor=doctor
        self.receta=receta

    def __str__(self):
            return ("\n Sintomas:{}\n Nivel de dolor : {}\n posicion : {}\nDiagnostico:{}\nDoctor:{}\n Receta{}"
                    .format(self.sintomas,self.nivelDolor,self.posicion,self.diagnostico,self.doctor,self.receta))


listaPersonas =[]
citas = []
atencionpaciente = []
recetas = []

#Medicos
medico1 = Persona ("207790516","Cristian","crisov1998","19/05/1998",
                   "cristianov19@gmail.com","Cedral",19,"Masculino","8521-3563","Medico",)
listaPersonas.append(medico1)
medico2 = Persona("987","Alfonso","987","26/02/1998","dacripo98@gmail.com","Barrio Lourdes",
                  25,"Masculino","8879-4982","Medico")
#Secretarias
gloria = Persona (111,"Gloria","111","1995/04/05","gloria@gmail.com","Barrio los Angeles",24,"M","2460-54-51","secretaria",)
listaPersonas.append(gloria)
maria = Persona (321,"Maria","321","1998/04/19","chamo@gmail.com","Cedral",19,"M","2460-29-11","secretaria")
listaPersonas.append(maria)

#Pacientes y diagnostico:
pac = paciente(456,"Rodolfo","04/10/98","sacodecaca@cr.com","El bajo del Soncho",25,
               "Masculino","8865-4435","Hemorroides Cronica",medico1.nombre)
cita = Citas("19/8/17",4,medico1.nombre)
pac.citaPac(cita)
rece = Receta("Alka-D","3 veces al dia cada 8 hrs","4 dias")
pac.medicamento(rece)
atencion = AtencionPaciente("Esfinter sensible","10","Ano","Diarrea",medico1.nombre,rece)
pac.atender(atencion)

print(pac)


def menuInicio(listaPersonas):
    while True:
        try:
            print("\n1-Iniciar sesion\n"
                  "2-Registrarse\n"
                  "3-Salir\n")
            opMenuIni = int(input("Seleccione una opcion:"))
            if opMenuIni == 1:
                while True:
                    valorI = 0
                    valorC = 0
                    valorT = 0
                    name = ""
                    while True:
                        try:
                            cedula = int(input("Digite su número de cedula: "))
                            break
                        except ValueError:
                            print("\n\nMAMON!\nNO PONGAS LETRAS EN LA CEDULA!!!\n")
                    while True:
                        try:
                            contraseña = str(input("Digite su contraseña: "))
                            if contraseña.isalnum():
                                break
                            else:
                                print("\n\n      ¡Error!\nSolo puedes usar numeros y letras\n")
                        except:
                            print("no no ")
                    for i in listaPersonas:
                        if i.id == cedula:
                            valorI = True
                            name = i.nombre
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
                            elif i.contraseña == contraseña:
                                valorC = False
                            elif i.id != cedula:
                                valorI = False

                    if valorI == True and valorC == True and valorT == True:
                        print("\nCedula y Contraseña correctas\n")
                        print("\nBienvenido(a) {}\n".format(name))
                        menuPrincipalMedicos(listaPersonas)

                    elif valorI == True and valorC == True and valorT == False:
                        print("\nCedula y Contraseña correctas")
                        print("\nBienvenido(a) {}\n".format(name))
                        menuPrincipalSecretaria(listaPersonas, listaCitas)

                    elif valorI == False and valorC == True:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == True and valorC == False:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == False and valorC == False:
                        print("\nCedula o contraseña invalida\n")
            elif opMenuIni== 2:
                id = str(input("Digite la cedula: "))
                contraseña = str(input("Digite la contraseña: "))
                nombre = str(input("Digite el nombre: "))
                fechaNacimiento = str(input("Digete  la fecha de nacimiento: "))
                correo = str(input("Digete el correo: "))
                direccion = str(input("Digite la dirección: "))
                edad = int(input("Digite la edad:"))
                genero = str(input("Digite el genero: "))
                telefono = str(input("Digite el telefono : "))
                tipoUsuario = str(input("Digete el tipo de usuario : "))
                padecimiento = str(input("Digete si tiene algun padecimiento:"))
                objregistro = Persona(id, nombre, contraseña, fechaNacimiento, correo, direccion, edad, genero,
                                      telefono, tipoUsuario,)
                listaPersonas.append(objregistro)

                menuInicio(listaPersonas, listaCitas)

            elif opMenuIni == 3:
                print("\n\nGracias por preferirnos\n")
                break
        except ValueError:
            print("\n\nMe cago en TODO lo que se menea\nNO DEBES PONER LETRAS O MUCHOS NUMEROS A LA VEZ\nSTEEE MENNNN  :V")
#LISTO!!


#LISTO!!

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
       existe = ""
       existe2 = ""
       doc = ""
       nombre = ""
       while True:
           while True:
               try:
                   cedula = int(input("Digite el número de cedula: "))
                   if (cedula > 999999999) or (cedula < 100000000):
                       print("\n\nLa cedula debe tener '9' digitos\n\nSUBNORMAL!!\n\n"
                             "En caso de tener cedula de Extranjero,\n comuniquese con el area de 'TI"
                             "\n\n Gracias..")
                   else:
                       for i in listaPersonas:
                           if i.id == id:
                               existe = True
                               break
                           elif i.id != id:
                               existe = False
                       if existe == True:
                           print("\n\nLa cedula esta ya registrada.\n\n")
                       break
               except ValueError:
                   print("\n\nMAMON!\nNO PONGAS LETRAS EN LA CEDULA!!!\n")

           while True:
               try:
                   nombre = str(input("Digite el nombre: "))
                   if nombre.isalpha():
                       break
                   else:
                       print("\n\nNo pueden haber numeros o simbolos en un nombre\n\n")
               except:
                   print("Valor invalido")

           while True:
               try:
                   fechaNacimiento = str(input("Digete la fecha :"))
                   for v in fechaNacimiento:
                       if v.isalpha():
                           print("Esta Fecha {}, contiene letras..."
                                 "\nEL FORMATO DE FECHA ES ASI: dd/mm/aaaa"
                                 "\n\nMAMON\n\nDigite de nuevo.".format(fechaNacimiento))
                           break
                       else:
                           pass
                   break
               except:
                   pass

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
               Paciente = paciente(cedula, )
               print(listaCitas[-1])
               break
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


    


                        #1.1.2.3






# Programa Principal:

print(time.strftime("%x"))
menuInicio(listaPersonas)

#time.strftime("%I:%M:%S")#hora



