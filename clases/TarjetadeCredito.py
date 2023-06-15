class TarjetadeCredito:
    def __init__(self, Nombre_tarjeta, monto):
        self._Nombre_tarjeta = Nombre_tarjeta
        self._monto = monto

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto

    @property
    def Nombre_tarjeta(self):
        return self._Nombre_tarjeta

    @Nombre_tarjeta.setter
    def Nombre_tarjeta(self, Nombre_tarjeta):
        self._Nombre_tarjeta = Nombre_tarjeta

    def __str__(self):
        return f'Nombre de la tarjeta: {self._Nombre_tarjeta}, monto: ${self._monto}'







