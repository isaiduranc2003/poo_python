#instancias
class Perros (object):
    'Clase para los perros' #Descripcion
    Collar = True #Variable de clase Estática
    def __init__(self, salud, hambre):
        self.salud = salud #Variable de Instancia
        self.hambre = hambre #Variable de Instancia

Dogo = Perros(100, 50)
print(Dogo.hambre)
