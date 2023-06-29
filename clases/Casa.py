from clases.Gasto import Gasto


class Casa(Gasto):
    def __init__(self, impuestos, servicios, alquiler, alimentos):
        self._impuestos = impuestos
        self._servicios = servicios
        self._alquiler = alquiler
        self._alimentos = alimentos
        self._monto = self._impuestos + self._servicios + self._alquiler + self._alimentos

    def __str__(self):
        return f"-> Gastos de la casa\n" \
               f"\n- Impuestos: ${self._impuestos}" \
               f"\n- Servicios: ${self._servicios}" \
               f"\n- Alquiler: ${self._alquiler}" \
               f"\n- Alimentos: ${self._alimentos}"

    def mostrar_detalle(self):
        return self.__str__()

    # METODOS GETTER AND SETTER
    @property
    def monto(self):
        return self._monto

    @property
    def impuestos(self):
        return self._impuestos

    @impuestos.setter
    def impuestos(self, impuestos):
        self._impuestos = impuestos

    @property
    def servicios(self):
        return self._servicios

    @servicios.setter
    def servicios(self, servicios):
        self._servicios = servicios

    @property
    def alquiler(self):
        return self._alquiler

    @alquiler.setter
    def alquiler(self, alquiler):
        self._alquiler = alquiler

    @property
    def alimentos(self):
        return self._alimentos

    @alimentos.setter
    def alimentos(self, alimentos):
        self._alimentos = alimentos

