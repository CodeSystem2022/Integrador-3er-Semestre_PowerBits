class Educacion:
    def __init__(self, monto):
        self._monto = monto

    def __str__(self):
        return f'Monto: ${self._monto}'

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto 