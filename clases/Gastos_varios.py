from clases.Gasto import Gasto

# Creamos la clase gastos_varios que hereda de la clase padre Gasto
class Gastos_varios(Gasto):

    # Inicializamos el objeto y le pasamos los parámetros
    # Los parámetros los utilizamos para establecer las variables de instancia
    def __init__(self, detalle, monto_gastos_varios):
        self._detalle = detalle
        self._monto_gastos_varios = monto_gastos_varios

    # El método __str__ proporciona una cadena que incluye los detalles del gasto y el monto
    def __str__(self):
        return f"-> Gastos varios\n" \
               f"\n- Detalle de la compra: {self._detalle} " \
               f"\n- Monto: ${self._monto_gastos_varios}"

    # Método que llama al __str__ y devuelve su resultado
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

    @monto_gastos_varios.setter
    def monto_gastos_varios(self, monto_gastos_varios):
        self._monto_gastos_varios = monto_gastos_varios
