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

pacientes={}

p=Persona("123","cris","123","1995/04/05","andre@gmail.com","Barrio los Angeles",24,"M","2460-54-51","medico","No tengo")
pacientes[p.id]=p

p = Persona ("123","gloria","123","1995/04/05","gloria@gmail.com","Barrio los Angeles",24,"M","2460-54-51","secretaria","No tengo")
pacientes[p.id]=p

menu = ("Menu - Consultorio Médico\n"
        "1. Registro de pacientes\n"
        "  Seleccione una opción: ")
while True:
    print("\n\n\n")
    op = int(input(menu))
    print("\n\n")
    if op == 1:
        print("Complete los datos del paciente\n")
        id = str(input("Digite la cedula del paciente: "))
        nombre = str(input("Digite el nombre del paciente: "))
        contraseña=str(input("Digite la contraseña del paciente: "))
        fechaNacimiento = str(input("Digete  la fecha de nacimiento del paciente: "))
        correo = str(input("Digete el correo del paciente: "))
        direccion = str(input("Digite la dirección del paciente: "))
        edad = int(input("Digite la edad del paciente :"))
        genero = str(input("Digite el genero del paciente: "))
        telefono = str(input("Digite el telefono del paciente : "))
        tipoUsuario = str(input("Digite el Tipo de Usuario:"))
        padecimiento = str(input("Digete el padecimiento: "))
        p = Persona(id,nombre,contraseña,fechaNacimiento,correo,direccion,edad,genero,telefono,tipoUsuario,padecimiento)
        pacientes[p.id] = p
        print (pacientes)



