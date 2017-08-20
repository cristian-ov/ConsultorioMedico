import time

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
                 telefono,padecimiento,medico,tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.padecimiento = padecimiento
        self.medico = medico
        self.tipo_usuario = tipo_usuario
        self.cita= []
        self.atencionpaciente = []
        self.recetas =[]
        
    def medicamento (self,receta):
        self.recetas.append(receta)

    def atender (self,atencion):
        self.atencionpaciente.append(atencion)

    def citaPac(self,cita):
        self.cita.append(cita)

    def __str__(self):
        ci = ""
        at = ""
        re = ""
        for c in self.cita:
            ci = c
        for a in self.atencionpaciente:
            at = a
        for r in self.recetas:
            re = r

        return ("Expediente:\n\nCedula = {}\nNombre = {}\nFecha de Nacimiento = {}\n"
                "Padecimiento = {}\nTipo de usuario: {}\nMedico = {}\n\nCitas:\n{}\nDiagnostico:\n{}\n\nRecetas:\n{}"
                .format(self.id,self.nombre,self.fechaNacimiento,self.padecimiento,self.tipo_usuario,self.medico,ci,at,re))
class Citas:
    def __init__(self,fecha,hora,doctor):
        self.fecha=fecha
        self.hora=hora
        self.doctor=doctor

    def __str__(self):
        return ("Fecha = {}\nHora = {}"
                "\nMedico = {}\n".format(self.fecha,self.hora,self.doctor))
class Receta:
    def __init__(self,nombreMedi,formaMedi,cantiDias):
        self.nombreMedi=nombreMedi
        self.formaMedi=formaMedi
        self.cantiDias=cantiDias

    def __str__(self):
            return ("Medicamento : {}\nForma de tomar el medicamento: {}\nCantidad de Dias: {}\n "
                    .format(self.nombreMedi, self.formaMedi,self.cantiDias))
class AtencionPaciente:
    def __init__(self,sintomas,nivelDolor,posicion,diagnostico,doctor):
        self.sintomas=sintomas
        self.nivelDolor=nivelDolor
        self.posicion=posicion
        self.diagnostico=diagnostico
        self.doctor=doctor

    def __str__(self):
            return ("Sintomas:{}\nNivel de dolor: {}\nPosicion: {}\nDiagnostico: {}\nDoctor: {}"
                    .format(self.sintomas,self.nivelDolor,self.posicion,self.diagnostico,self.doctor))

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
               "Masculino","8865-4435","Hemorroides Cronica","Paciente",medico1.nombre)
listaPersonas.append(pac)
cita = Citas("19/8/17","04",medico1.nombre)
pac.citaPac(cita)
citas.append(cita)


rece = Receta("Alka-D","3 veces al dia cada 8 hrs","4 dias")
pac.medicamento(rece)
recetas.append(rece)


atencion = AtencionPaciente("Esfinter sensible","10","Ano","Diarrea",medico1.nombre)
pac.atender(atencion)
atencionpaciente.append(atencion)




def menuInicio(listaPersonas,citas,atencionpaciente,recetas):
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
                        menuPrincipalMedicos(listaPersonas,citas,atencionpaciente,recetas)

                    elif valorI == True and valorC == True and valorT == False:
                        print("\nCedula y Contraseña correctas")
                        print("\nBienvenido(a) {}\n".format(name))
                        menuPrincipalSecretaria(listaPersonas,citas,atencionpaciente,recetas)

                    elif valorI == False and valorC == True:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == True and valorC == False:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == False and valorC == False:
                        print("\nCedula o contraseña invalida\n")
            elif opMenuIni== 2: #Validar
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
                objregistro = Persona(id, nombre, contraseña, fechaNacimiento, correo, direccion, edad, genero,
                                      telefono, tipoUsuario,)
                listaPersonas.append(objregistro)

                menuInicio(listaPersonas,citas,atencionpaciente,recetas)
            elif opMenuIni ==3:
                cedula = str(input("Digete la cedula:"))
                for x in listaPersonas:
                    if x.id == cedula:
                        menuPrincipalPaciente(listaPersonas)

                    elif x.id != cedula:
                        print("Cedula invalida")
                        menuInicio(listaPersonas,citas,atencionpaciente,recetas)
            elif opMenuIni == 4:
                print("\n\nGracias por preferirnos\n")
                break
        except ValueError:
            print("\n\nMe cago en TODO lo que se menea\nNO DEBES PONER LETRAS O MUCHOS NUMEROS A LA VEZ\nSTEEE MENNNN  :V")
#LISTO!!



def menuPrincipalMedicos (listaPersonas,citas,atencionpaciente,recetas):#1.1.1

    print("1-Consultar citas\n"
                "2-Registrar cita\n"
                "3-Atender Pacientes\n"
                "4-Recetas\n"
                 "5-Salir\n")

    opMedico=input("Seleccione  una opcion : " )
    if opMedico == "1":
        print("Menu\n"
              "Seleccione una opcion :\n"
              "1-Citas del dia\n"
              "2-Fecha expecifica\n"
              "3-Salir")
        opCita = int(input("Seleccione una opcion: "))

        if opCita == 1:
            result = ""
            for x in citas:
                if x.fecha == time.strftime("%x"):
                    result += x.id + " " + x.paciente + " " + x.hora
                    result += "\n"
                    print("Cedula:{}\nPaciente:{}\nHora:{}".format(x.id, x.paciente, x.hora))
                elif x.fecha != time.strftime("&x"):
                    print("No tiene citas ")
        elif opCita == 2:
            fecha = str(input("Digite la fecha:"))
            result = ""
            for x in citas:
                if x.fecha == fecha:
                    result += x.id + " " + x.paciente + " " + x.hora
                    result += "\n"
                    print("Cedula:{}\nPaciente:{}\nHora:{}".format(x.id, x.paciente, x.hora))
                elif x.fecha != fecha:
                    print("No tiene Citas esta fecha")
        elif opCita == 3:
            print("Gracias por preferirnos\n")
            menuPrincipalMedicos(listaPersonas,citas)

    elif opMedico == "2":
        while True:
            ced = str(input("Digite la cedula :"))
            for x in listaPersonas:
               if ced == x.id:
                   print("Paciente:  ",x.nombre)
                    for i in x.cita:
                        fecha = str(input("Digete la fecha :"))
                        hora = str(input("Digete la hora :"))
                        padecimiento = (input("Digete el padecimiento : "))
                        doctor = input("Digete el nombre del doctor: ")
                        registroCitas = Citas(id, paciente, fecha, hora, padecimiento, doctor)
                        listaCitas.append(registroCitas)
                        print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\npadecimiento:{}\ndoctor:{}".format(id, paciente, fecha,
                                                                                                              hora,
                                                                                                              padecimiento, doctor))
                        op = input("Desea registrar otra cita s/n ")
                        if op == "s":
                            pass
                        elif op == "n":
                            menuPrincipalSecretaria(listaPersonas, listaCitas)
                            break
                        else:
                            print("Valor invalido")
    elif opMedico =="3":
        v=""
        cedula = int(input("cedula: "))
        for x in listaPersonas:
            if cedula == x.id:
                for i in x.cita:
                    if time.strftime("%x") == i.fecha and time.strftime("%I") == i.hora:
                        print("usted esta a tiempo para la cita")
                        fecha = str(input("Digete la fecha:"))
                        sintomas = str(input("Digete los sintomas: "))
                        nivelDolor = str(input("Digete el nivel de dolor:"))  # Rango de dolor
                        posicion = str(input("Digete la posicion:"))  # Area
                        diagnostico = str(input("Digete el diagnostico:"))
                        doctor = str(input("Digete el doctor"))
                        receta = str(input("Digete la receta"))
                        break#Terminar
                    elif time.strftime("%x") != i.fecha or (time.strftime("%I") != i.hora or time.strftime("%I") < x.hora):
                        print("Cita no registrada o atrasada")
            if cedula != x.id:
                v = False
        if v == False:
            print("id no esta en lista")

    elif opMedico =="4":
        pass
    elif opMedico =="5":
        print("Gracias por preferirnos")

    menuInicio(listaPersonas,citas,atencionpaciente,recetas)

def menuPrincipalSecretaria(listaPersonas,citas,atencionpaciente,recetas):

   print("\n1-Registrar cita\n"
                   "2-Imprimir comprobante\n"
                   "3-Registrar paciente \n"
                   "4-Salir\n ")


   opSecretaria=input("Seleccione una opcion: ")

   if opSecretaria == "1":
       while True:
           id = str(input("Digite la cedula :"))
           fecha = str(input("Digete la fecha :"))
           hora = str(input("Digete la hora :"))
           padecimiento = (input("Digete el padecimiento : "))
           doctor = input("Digete el nombre del doctor: ")
           registroCitas = Citas(fecha, hora, doctor)
           citas.append(registroCitas)
           print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\npadecimiento:{}\ndoctor:{}".format(id, paciente, fecha,
                                                                                                 hora,
                                                                                                 padecimiento, doctor))
           op = input("Desea registrar otra cita s/n ")
           if op == "s":
               pass
           elif op == "n":
               menuPrincipalSecretaria(listaPersonas, citas)
               break
           else:
               print("Valor invalido")

   elif opSecretaria == "2":
       cedula = str(input("Digete la cedula del paciente: "))
       fecha = str(input("Digete la fecha de la cita: "))
       for x in atencionpaciente:
           if x.id == cedula and x.fecha == fecha:
               print("Nombre del paciente: {}\nConsultorio medico: Digitaldoctor\n"
                     "Medico: {}\nFecha: {}\nDiagnostico: {}"
                     .format(x.nombre, x.doctor, x.fecha, x.diagnostico))
               menuPrincipalSecretaria(listaPersonas,citas,atencionpaciente,recetas)
               break

           elif x.id != cedula and x.fecha != fecha:
               print("Cedula o fecha invalida")

           elif x.id == cedula and x.fecha != fecha:
               print("Cedula o fecha invalida")

           elif x.id != cedula and x.fecha == fecha:
               print("Cedula o fecha invalida")

   elif opSecretaria == "3":
       existe = ""
       existe2 = ""
       doc = ""
       nombre = ""
       while True:
           while True:
               try:
                   cedula = int(input("Datos Paciente:\n\nDigite el número de cedula: "))
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
           correo = str(input("Digete el correo: "))
           direccion = str(input("Digite la dirección: "))
           while True:
               edad = int(input("Digite la edad:"))
               try:
                   if edad <= 100:
                       break
                   elif edad > 100:
                       print("Edad Invalida")
               except ValueError:
                   print("Error")
           while True:
               genero = str(input("Digite el genero del paciente: "))
               try:
                   if genero == "Masculino" or genero == "Femenino":
                        break
                   elif genero != "Masculino" or genero != "Femenino":
                        print("Error Invalida")
               except:
                   print("Valor invalido")
           telefono = str(input("Digite el telefono: "))
           padecimiento = str(input("Digite el padecimiento: "))
           print("Doctores:")
           for t in listaPersonas:
               if t.tipo_usuario == "Medico":  # Revisar este proceso
                   print("Doctor:", t.nombre)

           doctor = input("Digete el nombre del doctor: ")
           for l in listaPersonas:
               if doctor == l.nombre:
                   existe2 = True
                   break
               elif doctor != l.nombre:
                   existe2 = False
               else:
                   existe2 = False
           if existe2 == True:
               Paciente = paciente(cedula,cedula,fechaNacimiento,correo,direccion,
                                   edad,genero,telefono,padecimiento,doctor)
               print(citas[-1])
               break

   elif opSecretaria == "4":
       print("Gracias por preferirnos")
       menuInicio(listaPersonas,citas,atencionpaciente,recetas)





def citasPendientes(citas):
    result = ""
    for x in citas:
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
                    pass
                elif opPaciente == 2:
                    pass
                elif opPaciente == 3:
                    for x in listaPersonas:
                        if x.tipo_usuario == "Paciente":
                            cedula = str(input("Digete la cedula:"))
                            menuPrincipalPaciente(listaPersonas)
                elif opPaciente == 4:
                    print ("Gracias por escogernos:")
                    menuInicio(listaPersonas)








                    #1.1.2
#opciones menu secretaria







# Programa Principal:

print(time.strftime("%x"))
menuInicio(listaPersonas,citas,atencionpaciente,recetas)

#time.strftime("%I:%M:%S")#hora



