#encapsulamienyo
class Ejemplo():
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):#no se puede ver ya que esta privado
        return "Soy un metodo privado, para ti no existo"
objeto = Ejemplo()
print(objeto.publico())
print(objeto.__privado())
