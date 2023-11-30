# uso de self
class Prueba():
  pass

p = Prueba()

print(type(Prueba))
print(type(p))
## usando self
class Persona:

    def __init__(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre: {0}".format(self.nombre))

p1 = Persona("Juan")
p2 = Persona("Pedro")
print(type(Persona))
print(type(p1))
print(type(p2))


class B:
  def __init__(self, numero):
    self.numero = numero
  @staticmethod
  def saludo():
    print('Hola')

B = B(10)
B.saludo()

