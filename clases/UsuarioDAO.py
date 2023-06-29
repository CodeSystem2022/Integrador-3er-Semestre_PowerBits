# -------------------------------------------------- DOCUMENTACIÓN ----------------------------------------------------
# A esta clase la utilizamos para poner "constantes" que contienen consultas query, con las que podemos interactuar con
# la base de datos.
# También hay métodos de la clase, los cuales realizar acciones como:
#   - iniciar sesión
#   - crear un usuario nuevo
#   - mostrar todos los usuarios
#   - mostrar solamente los datos del usuario que inicio sesión

# y que luego se van a agregar más, como pueden ser:
#   - actualizar usuario
#   - eliminar usuario


class UsuarioDAO2:
    """"
        DAO significa: Data Acces Object
        CRUD significa:
            Create -> Insertar
            Read -> Seleccionar
            Update -> Actualizar
            Delete -> Eliminar
    """

    # aca creamos variable que simulan una constante, con las consultas query, para poder conectarnos a la base de datos
    _MOSTRAR_USUARIOS = 'SELECT * FROM login ORDER BY id_usuario'
    _MOSTRAR_UN_USUARIO = 'SELECT id_usuario, nombre, apellido, email, monto_inicial, nombre_usuario, password ' \
                          'FROM login WHERE nombre_usuario=%s and password=%s'
    _INSERTAR_USUARIO = 'INSERT INTO login(nombre, apellido, email, monto_inicial, nombre_usuario, password) ' \
                        'VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR_USUARIO = 'UPDATE login SET ' \
                          'nombre=%s, apellido=%s, email=%s, monto_inicial=%s, nombre_usuario=%s, password=%s ' \
                          'WHERE nombre_usuario=%s'
    _ELIMINAR_USUARIO = 'DELETE FROM login WHERE nombre_usuario=%s'
    _INICIAR_SESION = 'SELECT * FROM login WHERE nombre_usuario = %s and password = %s'
    _ACTUALIZAR_USUARIO_ADMIN = 'UPDATE login SET ' \
                          'nombre=%s, apellido=%s, email=%s, monto_inicial=%s, nombre_usuario=%s, password=%s ' \
                          'WHERE id_usuario=%s'
    _LIMPIAR_USUARIOS = 'DELETE FROM login'


    @classmethod
    # este método recibe como argumentos las variables creadas en prueba2 y el cursor,
    # que están en la parte de iniciar sesión
    def iniciar_sesion(cls, usuario_registrado, password_registrado, cursor):
        # creamos una tupla de valores
        valores = (usuario_registrado, password_registrado)
        # ejecutamos la acción con el cursor, y le pasamos la sentencia de _INICIAR_SESION con el cls. (el cls se usa
        # para acceder a las variables de la clase), más la tupla de valores,
        # de esta manera el cursor va a hacer la consulta a la base de datos
        cursor.execute(cls._INICIAR_SESION, valores)
        # creamos una variable para almacenar por el momento, la cantidad de filas afectadas al realizar la acción,
        # esto se hace con el método fetchall
        resultados = cursor.fetchall()
        # y por ultimo retornamos el resultado
        return resultados
