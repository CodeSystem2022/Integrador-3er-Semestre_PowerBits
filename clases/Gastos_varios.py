from clases.Gasto import Gasto

class Gastos_varios(Gasto):
    def __init__(self, detalle, _monto_gastos_varios):
        self._detalle = detalle
        self._monto_gastos_varios = _monto_gastos_varios


    def __str__(self):
        return f"-> Gastos varios\n" \
               f"\n- Detalle de la compra: {self._detalle} " \
               f"\n- Monto: ${self._monto_gastos_varios}"


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
    def monto_gastos_varios(self):
        return self._monto_gastos_varios

    @monto.setter
    def monto_gastos_varios(self, monto_gastos_varios):
        self._monto_gastos_varios = monto_gastos_varios
