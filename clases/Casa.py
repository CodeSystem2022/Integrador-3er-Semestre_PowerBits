class Casa:
    def __init__(self, impuestos, servicios, alquiler):
        self._impuestos = impuestos
        self._servicios = servicios
        self._alquiler = alquiler

    def __str__(self):
        return f"\n-> Gastos de la casa" \
               f"\n- Impuestos: {self._impuestos}" \
               f"\n- Servicios: {self._servicios}" \
               f"\n- Alquiler: {self._alquiler}"

    def mostrar_detalle(self):
        return self.__str__()


    # METODOS GETTER AND SETTER
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

    # METODO PARA SUMAR TODO
    def monto_total(self):
        total = 0
        total = self._impuestos + self._servicios + self._alquiler
        return f"\n-> El monto total es: ${total}"


