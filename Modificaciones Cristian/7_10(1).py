import time

class Persona:
    def __init__(self,id,nombre,clave,fechaNacimiento,correo,direccion,edad,genero,telefono,tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.clave= clave
        self.fechaNacimiento = fechaNacimiento
        self.correo = correo
        self.direccion = direccion
        self.edad = edad
        self.genero = genero
        self.telefono = telefono
        self.tipo_usuario =tipo_usuario
        self.citas_del_dia = []

    def citas_medico(self,cita):
        self.citas_del_dia.append(cita)

    def __str__(self):
        cd =""
        for x in self.citas_del_dia:
            cd = x

        return ("Cedula = {}\n Nombre = {}\n contraseña = {}\n Fecha Nacimiento = {}\n "
                "Correo = {}\n Direccion = {}\n edad: {}\n genero: {}\n telefono: {}\n Tipo de usuario: {}\nCitas del doctor: {}".format(self.id,self.nombre,self.clave,
                                                              self.fechaNacimiento,self.correo,self.direccion,self.edad,self.genero,self.telefono,self.tipo_usuario,cd))
class paciente:
    def __init__(self,id,nombre,fechaNacimiento,correo,direcion,edad,genero,
                 telefono,tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.correo = correo
        self.direccion = direcion
        self.edad = edad
        self.genero = genero
        self.telefono=telefono
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

        return ("    Expediente Medico\n\nCedula: {}\nNombre: {}\nFecha de Nacimiento: {} "
                "\nCorreo: {}\nDireccion: {}\nEdad: {}\nGenero: {}\nTelefono: {}"
                "\nTipo de usuario: {}\n\nCitas:\n{}\nDiagnostico:\n{}\n\nRecetas:\n{}"
                .format(self.id,self.nombre,self.fechaNacimiento,self.correo,
                        self.direccion,self.edad,self.genero,self.telefono,self.tipo_usuario,ci,at,re))
class Citas:
    def __init__(self,fecha,hora,medico):
        self.fecha=fecha
        self.hora=hora
        self.medico=medico

    def __str__(self):
        return ("Fecha = {}\nHora = {}"
                "\nMedico = {}\n".format(self.fecha,self.hora,self.medico))
class Receta:
    def __init__(self,nombreMedi,formaMedi,cantiDias):
        self.nombreMedi=nombreMedi
        self.formaMedi=formaMedi
        self.cantiDias=cantiDias

    def __str__(self):
            return ("Medicamento : {}\nForma de tomar el medicamento: {}\nCantidad de Dias: {}\n "
                    .format(self.nombreMedi, self.formaMedi,self.cantiDias))
class AtencionPaciente:
    def __init__(self,padecimiento,sintomas,nivelDolor,posicion,diagnostico):
        self.padecimiento = padecimiento
        self.sintomas=sintomas
        self.nivelDolor=nivelDolor
        self.posicion=posicion
        self.diagnostico=diagnostico
    def __str__(self):
            return ("\nPadecimiento: {}\nSintomas:{}\nNivel de dolor: {}\nPosicion: {}\nDiagnostico: {}"
                    .format(self.padecimiento,self.sintomas,self.nivelDolor,self.posicion,self.diagnostico))

funcionarios =[]
pacientes =[]
citas = []
atencionpaciente = []
recetas = []

#Medicos
medico1 = Persona (123,"Cristian","123","19/05/1998",
                   "cristianov19@gmail.com","Cedral",19,"Masculino","8521-3563","Medico")
funcionarios.append(medico1)

medico2 = Persona(987,"Alfonso","987","26/02/1998","dacripo98@gmail.com","Barrio Lourdes",
                  25,"Masculino","8879-4982","Medico")
funcionarios.append(medico2)
#Secretarias
gloria = Persona (111,"Gloria","111","1995/04/05","gloria@gmail.com","Barrio los Angeles",24,"M","2460-54-51","secretaria",)
funcionarios.append(gloria)
maria = Persona (321,"Maria","321","1998/04/19","chamo@gmail.com","Cedral",19,"M","2460-29-11","secretaria")
funcionarios.append(maria)

#Pacientes y diagnostico:
pac = paciente(456,"Rodolfo","04/10/98","sacodecaca@cr.com","El bajo del Soncho",25,
               "Masculino","8865-4435","Paciente")
pacientes.append(pac)

cita = Citas("08/21/17","11",medico1.nombre)
pac.citaPac(cita)
citas.append(cita)
medico1.citas_medico(cita)

atencion = AtencionPaciente("Hemorroides Cronica","Esfinter sensible","10","Ano","Diarrea")
pac.atender(atencion)

atencionpaciente.append(atencion)

rece = Receta("Alka-D","3 veces al dia cada 8 hrs","4 dias")
pac.medicamento(rece)
recetas.append(rece)

def buscar_cedula_paciente(pacientes,cedula):
    v = ""
    for x in pacientes:
        if cedula == x.id:
            v = True
        elif cedula != x.id:
            v = False
    return v

def buscar_cedula_funcionario(funcionarios,cedula):
    v = ""
    for x in funcionarios:
        if cedula == x.id:
            v = True
            break
        elif cedula != x.id:
            v = False
    return v

"""while True:
    try:
        pass
    except ValueError:
        print("Error")"""
def menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas):
    while True:
        try:
            print("\n1-Iniciar sesion\n"
                  "2-Registrarse\n"
                  "3-Consultas de Paciente\n"
                  "4-Salir")
            opMenuIni = int(input("Seleccione una opcion:"))
            if opMenuIni == 1:
                while True:
                    valorI = 0
                    valorC = 0
                    valorT = 0
                    name = ""
                    medico =""
                    secretaria = ""
                    while True:
                        try:
                            cedula = int(input("Digite su número de cedula: "))
                            break
                        except ValueError:
                            print("\n\nNO PONGAS LETRAS EN LA CEDULA!!!\n")
                    while True:
                        try:
                            clave = str(input("Digite su contraseña: "))
                            if clave.isalnum():
                                break
                            else:
                                print("\n\n      ¡Error!\nSolo puedes usar numeros y letras\n")
                        except:
                            print("no no ")
                    for i in funcionarios:
                        if i.id == cedula:
                            valorI = True
                            name = i.nombre
                            if i.clave == clave:
                                valorC = True
                                if i.tipo_usuario == "Medico":
                                    valorT = True
                                    medico = i.nombre
                                    break
                                elif i.tipo_usuario == "Secretaria":
                                    valorT = False
                                    secretaria = i.nombre
                                    break

                            elif i.clave != clave:
                                valorC = False
                            elif i.clave == clave:
                                valorC = False
                            elif i.id != cedula:
                                valorI = False
                        elif i.id != cedula:
                            valorI = False

                    if valorI == True and valorC == True and valorT == True:
                        print("\nCedula y Contraseña correctas\n")
                        print("\nBienvenido(a) {}\n".format(name))
                        menuPrincipalMedicos(medico,funcionarios,pacientes,citas,atencionpaciente,recetas)

                    elif valorI == True and valorC == True and valorT == False:
                        print("\nCedula y Contraseña correctas")
                        print("\nBienvenido(a) {}\n".format(name))
                        menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas)

                    elif valorI == False and valorC == True:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == True and valorC == False:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == False and valorC == False:
                        print("\nCedula o contraseña invalida\n")

            elif opMenuIni== 2:
                while True:
                    while True:
                        try:
                            cedula = int(input("Digite su número de cedula: "))
                            if buscar_cedula_funcionario(funcionarios,cedula) == False:
                                break
                            if buscar_cedula_funcionario(funcionarios,cedula) == True:
                                print("Cedula ya registrada")
                        except ValueError:
                            print("\n\nNO PONGAS LETRAS EN LA CEDULA!!!\n\n")
                    while True:
                        try:
                            clave = str(input("Digite la contraseña: "))
                            break
                        except ValueError:
                            print("Error")
                    while True:
                        try:
                            nombre = str(input("Digite el nombre: "))
                            break
                        except ValueError:
                            print("\nERROR\n")
                    while True:
                        try:
                            fechaNacimiento = str(input("Digete  la fecha de nacimiento: "))
                            break
                        except ValueError:
                            print("\nERROR\n")

                    while True:
                        try:
                            correo = str(input("Digete el correo: "))
                            break
                        except ValueError:
                            print("\nERROR\n")
                    while True:
                        try:
                            direccion = str(input("Digite la dirección: "))
                            break
                        except ValueError:
                            print("\nERROR\n")
                    while True:
                        try:
                            edad = int(input("Digite la edad:"))
                            break
                        except ValueError:
                            print("\nERROR\n")
                    while True:
                        try:
                            genero = str(input("Digite el genero\n'Masculino' o 'Femenino': "))
                            if genero == "Masculino":
                                break
                            elif genero == "Femenino":
                                break
                            else:
                                print("Datos no validos")
                        except ValueError:
                            print("\nERROR\n")
                    while True:
                        try:
                            telefono = str(input("Digite el telefono : "))
                            break
                        except ValueError:
                            print("\nERROR\n")

                    while True:
                        try:
                            tipoUsuario = str(input("Digite el tipo de usuario\n'Medico' o 'Secretaria': "))
                            if tipoUsuario == "Medico":
                                break
                            elif tipoUsuario== "Secretaria":
                                break
                            else:
                                print("Datos no validos")
                        except ValueError:
                            print("\nERROR\n")
                    objregistro = Persona(cedula, nombre, clave, fechaNacimiento, correo, direccion, edad, genero,
                                          telefono, tipoUsuario,)
                    funcionarios.append(objregistro)

                    menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)

            elif opMenuIni == 3:
                v = ""
                while True:
                    try:
                        cedula = int(input("Digete la cedula:"))
                        if buscar_cedula_paciente(pacientes,cedula) == True:
                            menuPrincipalPaciente(funcionarios, pacientes, citas, atencionpaciente, recetas)
                            break
                        elif buscar_cedula_paciente(pacientes,cedula) == False:
                            print("Cedula invalida")
                            menuInicio(funcionarios, pacientes, citas, atencionpaciente, recetas)
                    except:
                        print("Datos Erroneos")

            elif opMenuIni == 4:
                print("\n\nGracias por preferirnos\n")
                break
            else:
                print("Error")
        except ValueError:
            print("\n\nNO DEBES PONER LETRAS O MUCHOS NUMEROS A LA VEZ\n")

def menuPrincipalMedicos (medico,funcionarios,pacientes,citas,atencionpaciente,recetas):

    print("1-Consultar citas\n"
                "2-Registrar cita\n"
                "3-Atender Pacientes\n"
                "4-Recetas\n"
                 "5-Salir\n")

    opMedico=str(input("Seleccione  una opcion : " ))
    while True:
        try:
            if opMedico == "1":
                while True:
                    print("Menu\n"
                      "Seleccione una opcion :\n"
                      "1-Citas del dia\n"
                      "2-Fecha expecifica\n"
                      "3-Salir")
                    try:
                        opCita = int(input("Seleccione una opcion: "))
                        if opCita == 1:
                            v = ""
                            for x in funcionarios:
                                if x.nombre == medico:
                                    for i in x.citas_del_dia:
                                        cont = 1
                                        if i.fecha == time.strftime("%x"):
                                            print("{}: Fecha: {} Hora: {}:00".format(cont,i.fecha,i.hora))
                                            cont +=1
                                        elif i.fecha != time.strftime("&x"):
                                            v = False
                                    if v == False:
                                        print("No tiene citas ")
                                    break

                        elif opCita == 2:
                            fecha = str(input("Digite la fecha:"))
                            v = ""
                            for x in funcionarios:
                                if x.nombre == medico:
                                    for i in x.citas_del_dia:
                                        cont = 1
                                        if i.fecha == time.strftime("%x"):
                                            print("{}: Fecha: {} Hora: {}:00".format(cont, i.fecha, i.hora))
                                            cont += 1
                                        elif i.fecha != time.strftime("&x"):
                                            v = False
                                    if v == False:
                                        print("No tiene citas ")
                                    break

                        elif opCita == 3:
                            menuPrincipalMedicos(medico,funcionarios,pacientes,citas,atencionpaciente,recetas)
                            break
                    except ValueError:
                        print("Valor invalido")

            elif opMedico == "2":
                v = ""
                while True:
                    while True:
                        ced = int(input("Digite la cedula :"))
                        try:
                            for x in pacientes:
                                if ced == x.id:
                                    print("Paciente: ",x.nombre)#revisar For
                                    paciente =x.nombre
                                    while True:
                                        try:
                                            fecha = str(input("Digite la fecha :"))
                                            v2 = ""
                                            for i in x.cita:
                                                if i.fecha == fecha:
                                                    v2 = False
                                                elif i.fecha != fecha:
                                                    v2 = True
                                            if v2 == True:
                                                break
                                            elif v2 == False:
                                                print("Fecha ya registrada")
                                        except:
                                            print("Datos invalidos")
                                    hora = str(input("Digite la hora :"))
                                    registroCita = Citas(fecha, hora, medico)
                                    citas.append(registroCita)
                                    x.citaPac(registroCita)
                                    print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\ndoctor:{}"
                                          .format(ced, paciente, fecha, hora, medico))
                                    op = input("Desea registrar otra cita s/n ")
                                    if op == "s":
                                        pass
                                    elif op == "n":
                                        menuPrincipalMedicos(medico,funcionarios,pacientes,citas,atencionpaciente,recetas)
                                        break
                                    else:
                                        print("Valor invalido")
                                elif ced != x.id:
                                    v = False
                            if v == False:
                                print("no se encuentra cedula registrada")
                        except:
                            print("error")
            elif opMedico =="3":
                v=""
                v2 =""
                cedula = int(input("cedula: "))
                for x in pacientes:
                    if cedula == x.id:
                        for i in x.cita:
                            while True:
                                try:
                                    v3 = ""
                                    for h in x.cita:
                                        if h.medico == medico:
                                            v3 = True
                                            break
                                        elif h.medico != medico:
                                            v3=False
                                    if v3 == False:
                                        print("Este paciente no te corresponde")
                                    elif v3 == True:
                                        break
                                except:
                                    print("Error")

                            if time.strftime("%x") == i.fecha and time.strftime("%I") == i.hora:
                                print("usted esta a tiempo para la cita")
                                padecimiento = str(input("Digite el padecimiento: "))
                                sintomas = str(input("Digete los sintomas: "))
                                nivelDolor = str(input("Digete el nivel de dolor:"))
                                posicion = str(input("Digete la posicion:"))
                                diagnostico = str(input("Digete el diagnostico:"))
                                nMedicamento = str(input("Digete la receta:\nNombre del medicamento: "))
                                forma = str(input("Forma de uso: "))
                                dias = str(input("Durante cuanto tiempo: "))
                                rec=Receta(nMedicamento,forma,dias)
                                x.medicamento(rec)
                                recetas.append(rec)
                                registroAtenderPaciente = AtencionPaciente(padecimiento,sintomas, nivelDolor,
                                posicion, diagnostico)
                                x.atender(registroAtenderPaciente)
                                atencionpaciente.append(registroAtenderPaciente)
                                print(x)

                                break
                            elif time.strftime("%x") != i.fecha or (time.strftime("%I") != i.hora or time.strftime("%I") < x.hora):
                                v2 = False
                        if v2  == False:
                            print("Cita no registrada o atrasada")

                    if cedula != x.id:
                        v = False
                if v == False:
                    print("id no esta en lista")

            elif opMedico =="4":
                while True:
                    try:
                        v=""
                        ced = int(input("Digete la cedula del paciente: "))
                        for r in pacientes:  # recorre la lista pacientes
                            if ced == r.id:  # si la cedula es =  a la cedula en la lista pacientes
                                    nombreMedi = str(input("Digite el nombre del medicamento:"))
                                    formaMedi = str(input("Digite la forma de tomar el medicamento"))  # Recomendacion
                                    cantiDias = str(input("Digite la cantidad de dias:"))
                                    registrarReceta = Receta(nombreMedi, formaMedi,cantiDias)  # guardar en la variable  los datos de la clase receta
                                    citas.append(registrarReceta)  # guardar registrar receta en la lista citas
                                    print("nombre de Medicina:{}\nForma de tomar el medicamento:{}\nCantidad de Dias"
                                        .format(nombreMedi, formaMedi, cantiDias))
                                    break
                            elif ced != r.id:  # si la cedula es diferente a la cedula en la lista pacientes
                                v = False  # variable false
                            if v == False:  # si variable = false
                                print("Cedula invalida")
                    except ValueError:
                        print("Error")

            elif opMedico =="5":
                print("Gracias por preferirnos")
                menuInicio(funcionarios, pacientes, citas, atencionpaciente, recetas)
        except:
            print("Error en Menu medicos")

def menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas):

    print("\n1-Registrar cita\n"
                   "2-Imprimir comprobante\n"
                   "3-Registrar paciente \n"
                   "4-Salir\n ")


    opSecretaria=input("Seleccione una opcion: ")

    if opSecretaria == "1":
        while True:
           id = str(input("Digite la cedula :"))#verificar id y cantidad de citas semana
           fecha = str(input("Digete la fecha :"))
           hora = str(input("Digete la hora :"))
           padecimiento = (input("Digete el padecimiento : "))
           doctor = input("Digete el nombre del doctor: ")#validar doctor
           registroCitas = Citas(fecha, hora, doctor)
           citas.append(registroCitas)

           print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\npadecimiento:{}\ndoctor:{}".format(id, paciente, fecha,
                                                                                                 hora,
                                                                                                 padecimiento, doctor))
           op = input("Desea registrar otra cita s/n ")
           if op == "s":
               pass
           elif op == "n":
               menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas)
               break
           else:
               print("Valor invalido")
    ####
    elif opSecretaria == "2":
        v1 = ""
        v2 = ""
        while True:
            cedula = str(input("Digete la cedula del paciente: "))
            fecha = str(input("Digete la fecha de la cita: "))
            for x in pacientes:
                if x.id == cedula:
                    for i in atencionpaciente:
                        if x.fecha == fecha:
                            print("Nombre del paciente: {}\nConsultorio medico: Digitaldoctor\n"
                                    "Medico: {}\nFecha: {}\nDiagnostico: {}"
                                    .format(x.nombre, x.doctor, x.fecha, x.diagnostico))
                            menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas)
                            break
                        elif x.fecha != fecha:
                            v1 = False
                elif x.id != cedula :
                        v2 =False
            if v1 == False and v2 == False:
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
                           for i in pacientes:
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
               for t in funcionarios:
                   if t.tipo_usuario == "Medico":  # Revisar este proceso
                       print("Doctor:", t.nombre)

               doctor = input("Digete el nombre del doctor: ")
               for l in funcionarios:
                   if doctor == l.nombre:
                       existe2 = True
                       break
                   elif doctor != l.nombre:
                       existe2 = False
                   else:
                       existe2 = False
               if existe2 == True:
                   Paciente = paciente(cedula,nombre,fechaNacimiento,correo,direccion,
                                       edad,genero,telefono,"Paciente")#Revisar
                   print(citas[-1])
                   break
    ####
    elif opSecretaria == "4":
        print("Gracias por preferirnos")
        menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)

def menuPrincipalPaciente(funcionarios,pacientes,citas,atencionpaciente,recetas):

                print("1-Ultimas 3 recetas\n"
                      "2-Expediente Medico\n"
                      "3-Citas pendientes\n"
                      "4-Salir\n")

                opPaciente = int(input("Digete una opción: "))

                if opPaciente == 1:
                    pass #Con el -1        ####
                elif opPaciente == 2:
                    pass #esquema arriba   ####
                elif opPaciente == 3:
                    result = ""
                    for x in citas:
                        if x.fecha > time.strftime("%x") and x.hora > time.strftime("%I:%M:%S"):
                            result += x.fecha + " " + x.hora + " "
                            result += "\n"
                            print("Fecha:{}\nHora:{}".format(x.fecha, x.hora))
                        elif x.fecha < time.strftime("%x") and x.hora < time.strftime("%I:%M:%S"):
                            print("No tiene citas  pendientes")
                            menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)#terminar
                ####
                elif opPaciente == 4:
                    print ("Gracias por escogernos:")
                    menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)

# Programa Principal:

print(time.strftime("%x"))
menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)
