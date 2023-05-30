class Comida:
    def __init__(self, monto, detalles):
        self._monto = monto
        self._detalles = detalles
    def __str__(self):
        return f'monto: {self._monto}, detalles: {self._detalles}'

    def mostrar_detalles(self):
        return self._str_()

    # METODOS GETTER AND SETTER
    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto

    @property
    def detalles(self):
        return self._detalles

    @detalles.setter
    def detalles(self, detalles):
        self._detalles = detalles




