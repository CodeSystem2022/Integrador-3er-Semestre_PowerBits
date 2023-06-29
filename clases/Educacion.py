from clases.Gasto import Gasto


class Educacion(Gasto):
    def __init__(self, monto):
        self._monto = monto

    def __str__(self):
        return f'-> Gastos de educación\n' \
               f'\n- Monto: ${self._monto}'


    def mostrar_detalle(self):
        return self.__str__()

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto