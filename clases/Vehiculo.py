from clases.Gasto import Gasto


class Vehiculo(Gasto):
    def __init__(self, patente, combustible, seguro):
        self._patente = patente
        self._combustible = combustible
        self._seguro = seguro
        self._monto = self._patente + self._combustible + self._seguro

    def __str__(self):
        return f"-> Gastos del vehículo\n" \
               f"\n- Patente: ${self._patente}" \
               f"\n- Combustible: ${self._combustible}" \
               f"\n- Seguro: ${self._seguro}"

    def mostrar_detalle(self):
        return self.__str__()

    # GETTER AND SETTER
    @property
    def patente(self):
        return self._patente

    @patente.setter
    def patente(self, patente):
        self._patente = patente

    @property
    def combustible(self):
        return self._combustible

    @combustible.setter
    def combustible(self, combustible):
        self._combustible = combustible

    @property
    def seguro(self):
        return self._seguro

    @seguro.setter
    def seguro(self, seguro):
        self._seguro = seguro

    @property
    def monto(self):
        return self._monto

    # Calculamos el monto total
    def monto_total(self):
        total = 0
        total = self._patente + self._combustible + self._seguro
        return f"\n-> El monto total es: ${total}"