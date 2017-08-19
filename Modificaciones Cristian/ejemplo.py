class Paciente:
    def __init__(self, cedula, nombre, telefono, correo, sexo, tipo_sangre, fecha_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.sexo = sexo
        self.tipo_sangre = tipo_sangre
        self.fecha_nacimiento = fecha_nacimiento
        self.enfermedades = []

    def diagnostico(self, enfermedad):
        self.enfermedades.append(enfermedad)

    def __str__(self):
        return "{}: {} {} {}".format(self.cedula, self.nombre, self.sexo, self.fecha_nacimiento)


class Enfermedad:
    def __init__(self, nombre, sintomas):
        self.nombre = nombre
        self.sintomas = sintomas

    def __str__(self):
        return "{}: {}".format(self.nombre, self.sintomas)


pacientes = {}
enfermedades = {}
id_enfermedades = 1

# Datos de prueba
p = Paciente("206470762", "Allan Murillo Alfaro", "8526-2638", "allanmual@gmail.com", "M", "A+", "28/06/1988")
pacientes[p.cedula] = p
p = Paciente("206520946", "Lineth Matamoros Fernández", "8778-7857", "lineth.matamoros@gmail.com", "F", "O+",
             "17/11/1988")
pacientes[p.cedula] = p

e = Enfermedad("Bronquitis", "Tos")
enfermedades[id_enfermedades] = e
id_enfermedades += 1

e = Enfermedad("Gripe", "Fiebre alta")
enfermedades[id_enfermedades] = e
id_enfermedades += 1

e = Enfermedad("Dengue", "Vómitos")
enfermedades[id_enfermedades] = e
id_enfermedades += 1


def lista_pacientes(pacientes):
    texto = ""
    for x in pacientes:
        texto += "{}\n".format(pacientes[x])
    return texto


def lista_enfermedades(enfermedades):
    texto = ""
    for x in enfermedades:
        texto += "{}. {}\n".format(x, enfermedades[x].nombre)
    return texto


menu = ("Menu - Consultorio Médico\n"
        "1. Registro de pacientes\n"
        "2. Registro de enfermedades\n"
        "3. Diagnosticar paciente\n"
        "4. Listado de pacientes\n"
        "5. Pacientes por cédula\n"
        "6. Listado de enfermedades\n"
        "7. Salir\n"
        "   Seleccione una opción: ")

while True:
    print("\n\n\n")
    op = int(input(menu))
    print("\n\n")
    if op == 1:
        print("Complete los datos del paciente\n")
        ced = input("Cédula: ")
        nom = input("Nombre: ")
        tel = input("Teléfono: ")
        cor = input("Correo: ")
        sex = input("Sexo: \n(M) Masculino\n(F) Femenino")
        tip = input("Tipo de Sangre: ")
        fec = input("Fecha de Nacimiento: ")
        p = Paciente(ced, nom, tel, cor, sex, tip, fec)
        pacientes[p.cedula] = p
    elif op == 2:
        print("Complete los datos de la enfermedad\n")
        nom = input("Nombre: ")
        sin = input("Síntomas: ")
        e = Enfermedad(nom, sin)
        enfermedades[id_enfermedades] = e
        id_enfermedades += 1
    elif op == 3:
        ced = input("Digite la cédula del paciente: ")
        if ced in pacientes:
            print("Datos del paciente: " + str(pacientes[ced]))
            enf = int(input(lista_enfermedades(enfermedades) + "Seleccione la enfermedad a dignosticar: "))
            pacientes[ced].diagnostico(enfermedades[enf])
        else:
            print("Paciente no registrado")
    elif op == 4:
        print(lista_pacientes(pacientes))
    elif op == 5:
        ced = input("Digite la cédula del paciente: ")
        if ced in pacientes:
            print(pacientes[ced])
            for x in pacientes[ced].enfermedades:
                print("{}: {}".format(x.nombre, x.sintomas))
        else:
            print("Paciente no registrado")
    elif op == 6:
        print(lista_enfermedades(enfermedades))
    elif op == 7:
        break
