class EntradaDatos:
    contador_usuario = 0

    def __init__(self, nombre,apellido ,email,monto_inicial):
        EntradaDatos.contador_usuario +=1
        self._id_usuario = EntradaDatos.contador_usuario
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._monto_inicial = monto_inicial

    def __str__(self):
        return f"\nDatos del Usuario N°: {self._id_usuario}" \
               f"\nNombre: {self._nombre}" \
               f"\nApellido: {self._apellido}" \
               f"\nEmail: {self._email}" \
               f"\nMonto Inicial: {self._monto_inicial}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def monto_incial(self):
        return self._monto_inicial

    @monto_incial.setter
    def monto_inicial(self, monto_inicial):
        self._monto_inicial = monto_inicial