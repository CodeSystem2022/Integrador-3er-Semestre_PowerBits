class Usuario:
    contador_usuario = 0
    def __init__(self, nombre, apellido, email, monto_inicial, nombre_usuario, password):
        Usuario.contador_usuario += 1
        self._id_usuario = Usuario.contador_usuario
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._monto_inicial = monto_inicial
        self._nombre_usuario = nombre_usuario
        self._password = password

    def __str__(self):
        return f"\n-> Datos del Usuario:" \
               f"\n- id numero: {self._id_usuario}" \
               f"\n- Nombre: {self._nombre}" \
               f"\n- Apellido: {self._apellido}" \
               f"\n- Email: {self._email}" \
               f"\n- Monto Inicial: ${self._monto_inicial}"

    def mostrar_detalles(self):
        return self.__str__()

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
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
    def monto_inicial(self):
        return self._monto_inicial

    @monto_inicial.setter
    def monto_inicial(self, monto_inicial):
        self._monto_inicial = monto_inicial

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @nombre_usuario.setter
    def usuario(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def usuario(self, password):
        self._password = password