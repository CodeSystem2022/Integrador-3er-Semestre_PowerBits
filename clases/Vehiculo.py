from clases.Gasto import Gasto

class Vehiculo(Gasto):
    # Constructor de la clase Vehículo
    def __init__(self, patente, combustible, seguro):
        self._patente = patente
        self._combustible = combustible
        self._seguro = seguro
        self._monto = self._patente + self._combustible + self._seguro

    # Devuelve una cadena de texto del con los detalles de los gastos del
    # objeto vehículo (patente, combustible, seguro)
    def __str__(self):
        return f"-> Gastos del vehículo\n" \
               f"\n- Patente: ${self._patente}" \
               f"\n- Combustible: ${self._combustible}" \
               f"\n- Seguro: ${self._seguro}"

    # Asignamos el toString a un nuevo método para poder llamarlo posteriormente
    # Muestra el método __str__ anterior
    def mostrar_detalle(self):
        return self.__str__()

    # MÉTODOS GETTER AND SETTER
    @property
    def patente(self):
        return self._patente # Muestra el valor de la patente del vehículo

    @patente.setter
    def patente(self, patente):
        self._patente = patente # Sirve para modificar el valor de la patente del vehículo

    @property
    def combustible(self):
        return self._combustible # Muestra cuanto se gastó en combustible del vehículo

    @combustible.setter
    def combustible(self, combustible):
        self._combustible = combustible # Sirve para modificar el gasto en combustible del vehículo

    @property
    def seguro(self):
        return self._seguro # Muestra cuanto se gastó en seguro del vehículo

    @seguro.setter
    def seguro(self, seguro):
        self._seguro = seguro # Sirve para modificar el gasto en seguro del vehículo

    @property
    def monto(self):
        return self._monto # Muestra el monto total de los gastos del vehículo (patente + combustible + seguro)

    # Calculamos el monto total
    def monto_total(self):
        total = 0
        total = self._patente + self._combustible + self._seguro
        return f"\n-> El monto total es: ${total}"