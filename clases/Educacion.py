# Esta clase representa los gastos de educación. Se hereda de la clase Gasto.
from clases.Gasto import Gasto

# Tiene como atributos:
#   _monto (float): Monto de los gastos de educación.
# Tiene como métodos:
#   __init__(monto): Constructor de la clase.
#   __str__(): Devuelve una representación en cadena de los gastos.
#   mostrar_detalle(): Muestra los detalles de los gastos.
#   monto: Propiedad que permite obtener o modificar el monto de los gastos.

# Inicializa una instancia de la clase Educación.
# Utiliza el parámetro monto (float)
class Educacion(Gasto):
    def __init__(self, monto):
        self._monto = monto

# Devuelve una representación en cadena de los gastos de Educación y los detalles.
    def __str__(self):
        return f'-> Gastos de educación\n' \
               f'\n- Monto: ${self._monto}'

# Se muestran los detalles de los gastos de Educación.
    def mostrar_detalle(self):
        return self.__str__()

# Acá se encuentra la propiedad que permite obtener el monto de los gastos y se retorna el monto de los mismos.
    @property
    def monto(self):
        return self._monto

# Esta propiedad me permite modificar el monto de los gastos de educación.
# El parámetro utilizado es el monto (float); que es el nuevo monto de los gastos.
    @monto.setter
    def monto(self, monto):
        self._monto = monto