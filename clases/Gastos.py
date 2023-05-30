class Gastos:
    def __init__(self, ingresos,fijo_variable, mes):
        self._ingresos = ingresos
        self._fijo_variable = fijo_variable
        self._mes = mes


    def __str__(self):
        return f'Ingresos: {self._ingresos}, Fijo o variables: {self._fijo_variable}, Mes: {self._mes}'

    #Métodos Get/Set
    @property
    def ingresos(self):
        return self._ingresos

    @ingresos.setter
    def ingresos(self, ingresos):
         self._ingresos = ingresos

    @property
    def fijo_variable(self):
        return self._fijo_variable

    @fijo_variable.setter
    def ingresos(self, fijo_variable):
        self._fijo_variable = fijo_variable

    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, mes):
        self._mes = mes

    def mostrar_detalles(self):
        return self.__str__()

