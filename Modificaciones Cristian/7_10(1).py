import time #Libreria para verificar la fecha

#Creacion de clases
class Funcionario:
    def __init__(self,id,nombre,clave,fechaNacimiento,correo,direccion,edad,genero,telefono,tipo_usuario):#Atributos y constructor de clase Persona
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
        self.citas_del_dia = []#lista donde se guardaran las citas del doctor

    def citas_medico(self,cita):# metodo que añade las citas a la 'lista citas_del_dia'
        self.citas_del_dia.append(cita)

    def __str__(self):
        cd =""
        for x in self.citas_del_dia: #For para que se puedan imprimir los datos de 'citas_del_dia' en el metodo string
            cd = x

        return ("Cedula = {}\n Nombre = {}\n contraseña = {}\n Fecha Nacimiento = {}\n "
                "Correo = {}\n Direccion = {}\n edad: {}\n genero: {}\n telefono: {}\n Tipo de usuario: {}\nCitas del doctor: {}".format(self.id,self.nombre,self.clave,
                                                              self.fechaNacimiento,self.correo,self.direccion,self.edad,self.genero,self.telefono,self.tipo_usuario,cd))
class Paciente:
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
        #listas que guardaran los datos de las demas clase adjuntas abajo
        self.cita= []
        self.atencionpaciente = []
        self.recetas =[]

    #metodos que añade los datos de las demas clases en sus respectivas listas
    def medicamento (self,receta):
        self.recetas.append(receta)

    def atender (self,atencion):
        self.atencionpaciente.append(atencion)

    def citaPac(self,cita):
        self.cita.append(cita)

    def __str__(self):
        # For para que se puedan imprimir los datos en el metodo string
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
        return ("Fecha:{}\nHora: {}"
                "\nMedico: {}\n".format(self.fecha,self.hora,self.medico))
class Receta:
    def __init__(self,nombreMedi,formaMedi,cantiDias):
        self.nombreMedi=nombreMedi
        self.formaMedi=formaMedi
        self.cantiDias=cantiDias

    def __str__(self):
            return ("Medicamento: {}\nForma de tomar el medicamento: {}\nCantidad de Dias: {}\n "
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

#Listas en las que se guardaran los objetos
funcionarios =[]
pacientes =[]
citas = []
atencionpaciente = []
recetas = []

# Objetos Instanciados

#Medicos
medico1 = Funcionario (123,"Cristian","123","19/05/1998",
                   "cristianov19@gmail.com","Cedral",19,"Masculino","8521-3563","Medico")
funcionarios.append(medico1)

medico2 = Funcionario (987,"Alfonso","987","26/02/1998","dacripo98@gmail.com","Barrio Lourdes",
                  25,"Masculino","8879-4982","Medico")
funcionarios.append(medico2)

medico3=Funcionario(333, "Gloriana", "333", "04/12/1998", "dacripo98@gmail.com", "Barrio Lourdes",
                  25, "Femenino","8579-4982","Medico")
funcionarios.append(medico3)
#Secretarias
gloria = Funcionario (111,"Gloria","111","1995/04/05","gloria@gmail.com","Barrio los Angeles",24,"M","2460-54-51","secretaria",)
funcionarios.append(gloria)
maria = Funcionario (321,"Maria","321","1998/04/19","chamo@gmail.com","Cedral",19,"M","2460-29-11","secretaria")
funcionarios.append(maria)

# Pacientes:
#Paciente 1
pac1 = Paciente(456, "Rodolfo", "04/10/98", "sacodecaca@cr.com", "El bajo del Soncho", 25,"Masculino", "8865-4435","Paciente")
pacientes.append(pac1)#Ingresa los datos del paciente a la lista paciente
#Citas
cita1 = Citas("08/22/17", "05", medico1.nombre) #Ingresa los datos de la cita a la lista citas
pac1.citaPac(cita1)
citas.append(cita1)
#Atencion
atencion1 = AtencionPaciente("Esfinter sensible", "10", "Ano","Diarrea","Hemorroides cronica")#Ingresa los datos de atencion  a lista Atencion paciente
pac1.atender(atencion1)
atencionpaciente.append(atencion1)
#Recetas
rece1 = Receta("Alka-D", "3 veces al dia cada 8 hrs", "4 dias")
rece2 = Receta("Nogas","2 veces al dia cada 8 hrs","7 dias")
rece3 = Receta("Higadosanil","2 veces al dia cada 8 hrs","7 dias")
rece4 =  Receta("paracetamol","2 veces al dia cada 8 hrs","7 dias")
pac1.medicamento(rece1)
pac1.medicamento(rece2)
pac1.medicamento(rece3)
pac1.medicamento(rece4)
recetas.append(rece1)
recetas.append(rece2)
recetas.append(rece3)
recetas.append(rece4)


#Paciente 2
pac2= Paciente(789,"Ana","09/05/97","anita@gmail.com","San gerardo",18,"femenino","7085-2515","Paciente")
pacientes.append(pac2)#Ingresa los datos del paciente a la lista paciente
#Citas
cita2=Citas("08/25/17","05",medico2.nombre) #Ingresa los datos de la cita a la lista citas
pac2.citaPac(cita2)
citas.append(cita2)
#Atencion
atencion2= AtencionPaciente("Gripe","Moquera","4","Todo el cuerpo","Resfriado")#Ingresa los datos de la receta a lista recetas
pac2.atender(atencion2)
atencionpaciente.append(atencion2)
#Recetas
rece5= Receta("famotinina", "3 veces al dia cada 8 hrs", "4 dias")
rece6 = Receta("ibuprofeno","2 veces al dia cada 8 hrs","7 dias")
rece7 = Receta("tapcin","2 veces al dia cada 8 hrs","7 dias")
rece8 =  Receta("antifludes","2 veces al dia cada 8 hrs","7 dias")
pac2.medicamento(rece5)
pac2.medicamento(rece6)
pac2.medicamento(rece7)
pac2.medicamento(rece8)
recetas.append(rece5)
recetas.append(rece6)
recetas.append(rece7)
recetas.append(rece8)

#Objeto sin cita y sin recetas o diagnostico
#Paciente 3
pac3=Paciente(222,"Pepe","09/03/97","pepe@gmail.com","San gerardo",19,"Masculino","7585-2515","Paciente")
pacientes.append(pac3)#Ingresa los datos del paciente a la lista paciente

#metodo que verifica que una cedula este o no en la lista pacientee o funcionarios
def buscar_cedula_paciente(pacientes,cedula):
    v = ""
    for x in pacientes:
        if cedula == x.id:
            v = True
            break
        elif cedula != x.id:
            v = False
    return v #devuelve un valor Booleano en la variable v

def buscar_cedula_funcionario(funcionarios,cedula):
    v = ""
    for x in funcionarios:
        if cedula == x.id:
            v = True
            break
        elif cedula != x.id:
            v = False
    return v

#Menu Principal
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
                    #Valores para verificar los bucles For
                    valorI = 0
                    valorC = 0
                    valorT = 0
                    "Variables para extraer datos"
                    name = ""
                    medico =""
                    secretaria = ""
                    while True: #while True...try/except utilizado para validar los datos que son digitados por el usuario
                        try:
                            cedula = int(input("\nDigite su número de cedula: "))
                            break
                        except ValueError:
                            print("\n\nNO PONGAS LETRAS O SIMBOLOS EN LA CEDULA!!!\n")
                    while True:
                        try:
                            clave = str(input("Digite su contraseña: "))
                            if clave.isalnum():#Validacionde datos solo letras y numeros, no signos o simbolos
                                break
                            else:
                                print("\n\n      ¡Error!\nSolo puedes usar numeros y letras\n")
                        except:
                            print("Digiste Valores incorrectos ")
                    for i in funcionarios:#for que recorre los la lista funcionarios y verifica la informacion
                        if i.id == cedula:
                            valorI = True
                            name = i.nombre
                            if i.clave == clave:
                                valorC = True #booleanos para utilizar al alir del For
                                if i.tipo_usuario == "Medico":#Verificacion de medico
                                    valorT = True
                                    medico = i.nombre#Guarda la variable para identificarla al entrar al menu
                                    break
                                elif i.tipo_usuario == "Secretaria":#Verificacion de Secretaria
                                    valorT = False
                                    secretaria = i.nombre#Guarda la variable para identificarla al entrar al menu
                                    break

                            elif i.clave != clave:
                                valorC = False
                            elif i.clave == clave:
                                valorC = False
                            elif i.id != cedula:
                                valorI = False
                        elif i.id != cedula:
                            valorI = False

                    if valorI == True and valorC == True and valorT == True: #Validacion con booleanos para identificar medico de secretaria
                        print("\nCedula y Contraseña correctas\n")
                        print("\nBienvenido(a) {}\n".format(name))#utilizacion del i.nombre
                        menuPrincipalMedicos(medico,funcionarios,pacientes,citas,atencionpaciente,recetas)

                    elif valorI == True and valorC == True and valorT == False: #Validacion con booleanos
                        print("\nCedula y Contraseña correctas")
                        print("\nBienvenido(a) {}\n".format(name))#utilizacion del i.nombre
                        menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas)

                    elif valorI == False and valorC == True: #Validacion con booleanos en caso de cedula o contraseña no valida
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == True and valorC == False:
                        print("\nCedula o contraseña invalida\n")
                    elif valorI == False and valorC == False:
                        print("\nCedula o contraseña invalida\n")

            elif opMenuIni== 2:
                while True:
                    while True:
                        try:
                            cedula = int(input("\n\nDigite su número de cedula: "))
                            #retorna booleanos para validar cedula
                            if buscar_cedula_funcionario(funcionarios,cedula) == False:#utilizacion de los metodos buscar_cedula_funcionario
                                break
                            if buscar_cedula_funcionario(funcionarios,cedula) == True:#utilizacion de los metodos buscar_cedula_funcionario
                                print("Cedula ya registrada")
                        except ValueError:
                            print("\n\nNO PONGAS LETRAS EN LA CEDULA!!!\n\n")
                    while True:
                        try:
                            clave = str(input("Digite la contraseña: "))
                            break
                        except ValueError:
                            print("Datos incorrectos")
                    while True:
                        try:
                            nombre = str(input("Digite el nombre: "))
                            break
                        except ValueError:
                            print("\nDatos incorrectos\n")
                    while True:
                        try:
                            fechaNacimiento = str(input("Digete  la fecha de nacimiento: "))
                            break
                        except ValueError:
                            print("\nDatos incorrectos\n")

                    while True:
                        try:
                            correo = str(input("Digete el correo: "))
                            break
                        except ValueError:
                            print("\nDatos incorrectos\n")
                    while True:
                        try:
                            direccion = str(input("Digite la dirección: "))
                            break
                        except ValueError:
                            print("\nDatos incorrectos\n")
                    while True:
                        try:
                            edad = int(input("Digite la edad:"))
                            break
                        except ValueError:
                            print("\nDatos incorrectos (string)\n")
                    while True:
                        try:
                            genero = str(input("Digite el genero\n'Masculino' o 'Femenino': "))#Verificacion del genero
                            if genero == "Masculino":
                                break
                            elif genero == "Femenino":
                                break
                            else:
                                print("Datos no correctos a 'Masculino' o 'Femenino'")
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
                    objregistro = Funcionario (cedula, nombre, clave, fechaNacimiento, correo, direccion, edad, genero,
                                          telefono, tipoUsuario,)#instacia del objeto
                    funcionarios.append(objregistro)#agregado del objeto

                    menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)#menu incio

            elif opMenuIni == 3:
                while True:
                    try:
                        cedula = int(input("Digete la cedula:"))
                        if buscar_cedula_paciente(pacientes,cedula) == True: # Valida cedula y entra al menu de pacientes
                            menuPrincipalPaciente(cedula,funcionarios, pacientes, citas, atencionpaciente, recetas)#se le ingresa a los parametros la cedula para poder continuar
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
                print("Datos Erroneos")
        except ValueError:
            print("\n\nNO DEBES PONER LETRAS O MUCHOS NUMEROS A LA VEZ\n")
#menu Medicos
def menuPrincipalMedicos (medico,funcionarios,pacientes,citas,atencionpaciente,recetas):
    while True:
        print("      Menu Medicos\n\n"
              "1-Consultar citas\n"
              "2-Registrar cita\n"
              "3-Atender Pacientes\n"
              "4-Recetas\n"
              "5-Salir\n")

        opMedico = str(input("Seleccione  una opcion : "))
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
                        if opCita == 1:#Verifica citas del dia
                            v = ""
                            for x in funcionarios: # Verifica el nombre del medico para preguntar por sus citas
                                if x.nombre == medico:
                                    for i in x.citas_del_dia:
                                        cont = 1
                                        if i.fecha == time.strftime("%x"):#uso de la libreria time
                                            print("{}: Fecha: {} Hora: {}:00".format(cont,i.fecha,i.hora))#print para facilitar el uso de los datos
                                            cont +=1
                                        elif i.fecha != time.strftime("&x"):# "&x" muestra la fecha actual
                                             v = False
                                    if v == False:
                                        print("No tiene citas ")
                                    break

                        elif opCita == 2:
                            fecha = str(input("Digite la fecha:"))
                            v = ""
                            for x in funcionarios:
                                if x.nombre == medico:
                                    for i in x.citas_del_dia:#Revisa una fecha especifica en el atributo citas del dia de la clase funcionario
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
                                    print("Paciente: ",x.nombre)#Solo se necesita de la cedula para saber el nombre del paciente
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
                                    registroCita = Citas(fecha, hora, medico)#medico es una parametro heredado desde el menu inicio de sesion
                                    citas.append(registroCita)#los registra en la lista citas
                                    x.citaPac(registroCita)#mete el objeto en la variable cita con el metodo citaPac
                                    print("\nid: {}\npaciente: {}\nfecha: {}\nhora:{}\ndoctor:{}"
                                          .format(ced, paciente, fecha, hora, medico)) #modelo que imprime el resultado de la entrada de datos
                                    op = input("Desea registrar otra cita s/n ")#Pregunta en caso de volver a queres a registrar otra persona
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
                                        if h.medico == medico:#Valida que la cedula  que digito este con el nombre del medico
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

                            if time.strftime("%x") == i.fecha and time.strftime("%I") == i.hora:#Valida si esta tiempo para la cita
                                print("usted esta a tiempo para la cita")
                                padecimiento = str(input("Digite el padecimiento: "))
                                sintomas = str(input("Digete los sintomas: "))
                                nivelDolor = str(input("Digete el nivel de dolor:"))
                                posicion = str(input("Digete la posicion:"))
                                diagnostico = str(input("Digete el diagnostico:"))
                                while True:
                                    try:
                                        nMedicamento = str(input("Digete la receta:\nNombre del medicamento: "))
                                        forma = str(input("Forma de uso: "))
                                        dias = str(input("Durante cuanto tiempo: "))

                                        op = input("Desea registrar otra receta? s/n ")#Permite recetar varios medicamentos
                                        if op == "s":
                                            pass
                                        elif op == "n":
                                            menuPrincipalMedicos(medico, funcionarios, pacientes, citas, atencionpaciente,recetas)
                                            break
                                        else:
                                            print("Valor invalido")
                                    except:
                                        print("")
                                rec=Receta(nMedicamento,forma,dias)#Instancia del objeto
                                x.medicamento(rec)#se utiliza el metodo medicamento para guardar en la lista receta
                                recetas.append(rec)#se guarda el objeto en lista recetas
                                registroAtenderPaciente = AtencionPaciente(padecimiento,sintomas, nivelDolor,
                                posicion, diagnostico)#se añaden las recetas aparte del diagnostico
                                x.atender(registroAtenderPaciente)# metodo que guarda los datos en lista
                                atencionpaciente.append(registroAtenderPaciente)#guarda elementos en lista atencionpaciente
                                print(x)#muestra el objeto con el que hicimos el diagnostico

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
                        v4=""
                        ced = int(input("Digete la cedula del paciente: "))
                        for r in pacientes:  # recorre la lista pacientes
                            if ced == r.id:  # si la cedula es =  a la cedula en la lista pacientes
                                v4=True
                                nombreMedi = str(input("Digite el nombre del medicamento:"))
                                formaMedi = str(input("Digite la forma de tomar el medicamento: "))  # Recomendacion
                                cantiDias = str(input("Digite la cantidad de dias:"))
                                registrarReceta = Receta(nombreMedi, formaMedi,cantiDias)  # guardar en la variable  los datos de la clase receta
                                r.medicamento(registrarReceta)
                                recetas.append(registrarReceta)  # guardar registrar receta en la lista citas
                                print("\n\nNombre de Medicina: {}\nForma de tomar el medicamento: {}\nCantidad de Dias: {}\n\n"
                                        .format(nombreMedi, formaMedi, cantiDias))
                                break
                            elif ced != r.id:  # si la cedula es diferente a la cedula en la lista pacientes
                                v4 = False  # variable false
                        if v4 == False:  # si variable = false
                            print("Cedula invalida")
                        if v4 == True:
                            break
                    except ValueError:
                        print("Error")

            elif opMedico =="5":
                print("Gracias por preferirnos")
                menuInicio(funcionarios, pacientes, citas, atencionpaciente, recetas)
        except:
            print("Error en Menu medicos")
#Menu de Secretarias
def menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas):

    print("\n      Menu Secretarias\n\n"
          "1-Registrar cita\n"
            "2-Imprimir comprobante\n"
            "3-Registrar paciente \n"
            "4-Salir\n ")


    opSecretaria=input("Seleccione una opcion: ")

    if opSecretaria == "1":
        #Variables para usar con valores booleanos
        existe = ""
        existe2 = ""
        #variables para datos que se necesitan mover
        nombre = ""
        while True:
            try:
                ced = int(input("Digite la cedula :"))
                for i in pacientes:
                    if i.id == ced:
                        existe = True
                        nombre = i.nombre#Guarda el nombre para imprimirlo despues y identificar la cedula
                        print(nombre)
                        fecha = str(input("Digete la fecha :"))
                        hora = str(input("Digete la hora :"))
                        print("Doctores:")
                        for t in funcionarios:#muestra la lista de los doctores ya anteriormente instanciados
                            if t.tipo_usuario == "Medico":
                                print("Doctor:", t.nombre)
                        doctor = input("Digete el nombre del doctor: ")
                        for l in funcionarios:
                            if doctor == l.nombre:#Valida el nombre ingresado con el nombre de los medicos
                                existe2 = True
                                break
                            elif doctor != l.nombre:
                                existe2 = False
                        if existe2 == True:
                            registroCitas = Citas(fecha,hora,doctor)#instancia el objeto
                            i.citaPac(registroCitas)#llama al metodo para guardar en lista
                            citas.append(registroCitas)#guarda el objeto en lista
                            print(citas[-1])#imprime la ultima cita

                            op = input("Desea registrar otra cita s/n ")#Permite ingresar otra cita
                            if op == "s":
                                pass
                            elif op == "n":
                                menuPrincipalSecretaria(secretaria, funcionarios, pacientes, citas, atencionpaciente,
                                                        recetas)
                                break
                            else:
                                print("Valor invalido")

                        elif existe2 == False:
                            print("Valor invalido")
                        else:
                            print("Valor invalido")
                        break
                    elif i.id != ced:
                        existe = False
                if existe == True:
                    break
                elif existe == False:
                    print("cedula no registrada")
            except:
                print("Error")

    elif opSecretaria == "2":
        v1 = ""
        v2 = ""
        while True:
            try:
                cedula = int(input("Digete la cedula del paciente: "))
                for x in pacientes:#Validacion de que cedula este registrada para el comprobante
                    if x.id == cedula:
                        v1 = True
                        while True:
                            try:
                                fecha = str(input("Digete la fecha de la cita: "))
                                for f in x.cita:
                                    if f.fecha == fecha:
                                        v2 = True
                                        print("Nombre del paciente: {}\nConsultorio medico: Digitaldoctor\n"
                                              "Medico: {}\nFecha: {}"
                                              .format(x.nombre, f.medico, f.fecha))
                                        for j in x.atencionpaciente:
                                            print("\nDiagnostico: {}".format(j))
                                        menuPrincipalSecretaria(secretaria,funcionarios,pacientes,citas,atencionpaciente,recetas)
                                        break
                                    elif f.fecha != fecha:
                                        v2 = False
                                if v2 == True:
                                    break
                                elif v2 == False:
                                    print("Fecha no registrada")
                            except:
                                print("Valor invalido")
                    elif x.id != cedula:
                        v1 = False
                if v1 == False:
                    print("Cedula invalida")
                elif v1 == True:
                    break
            except:
                print("error")

    elif opSecretaria == "3":
        existe = ""
        existe2 = ""
        while True:
            try:
                while True:
                    print("\nDatos Paciente:")
                    try:
                        cedula = int(input("\nDigite el número de cedula: "))
                        if buscar_cedula_paciente(pacientes,cedula) == True:
                            print("cedula registrada")
                        elif buscar_cedula_paciente(pacientes, cedula) == False:
                            break
                    except:
                        print("Error")
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
                                         "\nEL FORMATO DE FECHA ES ASI: mm/dd/aa"
                                         "\n\nDigite de nuevo.".format(fechaNacimiento))
                                break
                            else:
                                pass
                        break
                    except:
                        pass
                correo = str(input("Digete el correo: "))
                direccion = str(input("Digite la dirección: "))
                while True:
                    try:
                        edad = int(input("Digite la edad:"))
                        if edad <= 100:
                            break
                        elif edad > 100:
                            print("Edad Invalida")
                    except ValueError:
                            print("Error")
                while True:
                    try:
                        genero = str(input("Digite el genero del paciente: "))
                        if genero == "Masculino" or genero == "Femenino":
                            break
                        elif genero != "Masculino" or genero != "Femenino":
                            print("Error Invalida")
                    except:
                        print("Valor invalido")
                telefono = str(input("Digite el telefono: "))
                registroPaciente = Paciente(cedula, nombre, fechaNacimiento, correo, direccion,
                                            edad, genero, telefono, "Paciente", )
                pacientes.append(registroPaciente)
                print("Cedula: {}\nNombre: {}\nFecha de nacimiento: {}\nCorreo: {}"
                        "\nDireccion: {}\nEdad: {}\nGenero: {}\nTelefono: {}"
                        "\nTipo de Usuario: Paciente".format(cedula, nombre,
                                                         fechaNacimiento, correo, direccion, edad, genero, telefono))
                menuPrincipalSecretaria(secretaria, funcionarios, pacientes, citas, atencionpaciente, recetas)
                break

            except:
                print("Error invalido")

    elif opSecretaria == "4":
        print("Gracias por preferirnos")
        menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)
#Menu de Pacientes
def menuPrincipalPaciente(cedula,funcionarios,pacientes,citas,atencionpaciente,recetas):

                print("1-Ultimas 3 recetas\n"
                      "2-Expediente Medico\n"
                      "3-Citas pendientes\n"
                      "4-Salir\n")

                opPaciente = int(input("Digete una opción: "))

                if opPaciente == 1:
                    while True:
                        cont = 1
                        v = ""
                        try:
                            for x in pacientes:
                                if x.id == cedula:
                                    v=True
                                    print("\n   Recetas\n")
                                    for i in x.recetas[-4:-1]:
                                        print("{}: {}".format(cont, i))
                                        cont += 1
                                    break

                                if x.id != cedula:
                                    v=False
                            if v== True:
                                menuPrincipalPaciente(cedula, funcionarios, pacientes, citas, atencionpaciente, recetas)
                                break
                            if v== False:
                                print("Cedula invalida")
                        except:
                            print("datos erroneos")

                elif opPaciente == 2:
                    for x in pacientes:
                        if x.id == cedula:
                            print(
                                "Expediente\n\nDatos personales:\nCedula: {}\nNombre: {}\nFecha de Nacimiento : {}\nCorreo:{}\nDireccion:{}\nEdad:{}\nGenero:{}\nTelefono:{}"
                                "\nTipo de usuario: {}".format(x.id, x.nombre, x.fechaNacimiento, x.correo,
                                                               x.direccion, x.edad, x.genero, x.telefono,
                                                               x.tipo_usuario))
                            print("Citas")
                            for i in x.cita:
                                print("{}\n".format(i))
                            print("Diagnostico")
                            for i in x.atencionpaciente:
                                print("{}\n".format(i))
                            print("Recetas")
                            for i in x.recetas:
                                print("{}\n".format(i))
                            menuPrincipalPaciente(cedula, funcionarios, pacientes, citas, atencionpaciente, recetas)
                            break

                elif opPaciente == 3:
                    while True:
                        try:
                            result = ""  # result vacia
                            v2 =""
                            for i in pacientes:
                                if i.id == cedula:
                                    v2= True
                                    for x in i.cita:  # recorre la lista de citas
                                        if x.fecha >= time.strftime("%x") and x.hora >= time.strftime("%I"):  # fecha en la lista de citas es mayor  a la fecha actual y la hora es mayor a la hora actual
                                            result += x.fecha + " " + x.hora + " "  # en result se guarda fecha y hora
                                            result += "\n"  # result enter
                                            print("Fecha:{}\nHora:{}".format(x.fecha, x.hora))
                                            break
                                        elif x.fecha < time.strftime("%x") and x.hora < time.strftime("%I"):  # fecha en la lista de citas es menor a la fecha actual y hora en la lista de citas es menor  a la hora actual
                                            print("No tiene citas  pendientes")
                                            menuInicio(funcionarios, pacientes, citas, atencionpaciente, recetas)
                                            break
                                elif i.id == cedula:
                                    v2 =  False
                            if  v2 == True:
                                break
                            elif v2 == False:
                                print("Cedula no registrada")
                        except:
                            print("Error")
                elif opPaciente == 4:
                    print ("Gracias por escogernos:")
                    menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)

# Programa Principal:

print(time.strftime("%x"))
print(time.strftime("%I:%M:%S"))
menuInicio(funcionarios,pacientes,citas,atencionpaciente,recetas)
