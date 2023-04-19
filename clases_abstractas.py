#clases abstractas
import abc
from abc import ABC
# Declaramos nuestra clase
class Animal(ABC):   
    # Asignar nombre
    def set_name(self, name):
        passS
    # Obtener nombre
    def get_name(self):
        pass
    # Definimos las propiedades
    name = abc.abstractproperty(get_name, set_name)
class Perro(Animal):  
    def __init__(self):
      pass    
    # Propiedad para obtener el nombre
    @property    
    def name(self):
        return self._name
    # Propiedad para asignar el nombre
    @name.setter
    def name(self, name):
        self._name = name
perro = Perro() # Instancia de Perro
perro.name = "Marly" # Asignación del nombre
print(perro.name) # Obtenemos el valor de name