class Id:
    def __init__(self,id):
        self.id=id
    def __str__(self):
        return "id: {}".format(self.id)


lista = []
iddd = Id(123)
lista.append(iddd)
iddd = Id(321)
lista.append(iddd)
iddd = Id(345)
lista.append(iddd)
v=""
ced = int(input("cedula: "))
for x in lista:
    if ced == x.id:
        v=True
        break
    if ced != x.id:
        v = False
if v == False:
    print("id no esta en lista")
nombre=input("nombre: ")
print("Cedula: {}\nNombre: {}".format(ced,nombre))