class Gastos_varios:
    def __init__(self, detalle, monto):
        self._detalle = detalle
        self._monto = monto


    def __str__(self):
        return f"Detalle: {self._detalle}, Monto: {self._monto}"

    def mostrar_detalles(self):
        return self.__str__()

    # METODOS GETTER AND SETTER
    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, detalle):
        self._detalle = detalle

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto
