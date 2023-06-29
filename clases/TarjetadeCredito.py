from clases.Gasto import Gasto


class TarjetaDeCredito(Gasto):
    def __init__(self, nombre_tarjeta, monto):
        self._nombre_tarjeta = nombre_tarjeta
        self._monto = monto

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto

    @property
    def nombre_tarjeta(self):
        return self._nombre_tarjeta

    @nombre_tarjeta.setter
    def nombre_tarjeta(self, nombre_tarjeta):
        self._nombre_tarjeta = nombre_tarjeta

    def __str__(self):
        return f'-> Gastos de la tarjeta de crédito\n' \
               f'\n- Nombre de la tarjeta: {self._nombre_tarjeta}' \
               f'\n- Monto: ${self._monto}'

    def mostrar_detalle(self):
        return self.__str__()














