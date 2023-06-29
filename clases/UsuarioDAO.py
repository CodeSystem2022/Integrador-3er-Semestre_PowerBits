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

    @classmethod
    # este método recibe el objeto creado en test y también el cursor,
    # para poder realizar la acción de agregar un usuario nuevo
    def agregar_usuario(cls, usuario_nuevo, cursor):
        # ahora, para poder crear la tupla con los valores que necesita la sentencia de _INSERTAR_USUARIO,
        # tenemos que acceder a cada atributo del objeto creado pero por separado
        valores = (usuario_nuevo.nombre,
                   usuario_nuevo.apellido,
                   usuario_nuevo.email,
                   usuario_nuevo.monto_inicial,
                   usuario_nuevo.nombre_usuario,
                   usuario_nuevo.password)
        # de esta forma podremos ejecutar la acción del cursor junto con los valores necesarios de la sentencia
        cursor.execute(cls._INSERTAR_USUARIO, valores)

    @classmethod
    # este método solo recibe el cursor, para poder realizar la acción
    def mostrar_usuarios(cls, cursor):
        # utilizamos la sentencia _SELECCIONAR, para que tome todos los usuarios registrados en la base de datos
        cursor.execute(cls._MOSTRAR_USUARIOS)
        # aca al utilizar _SELECCIONAR, se van a guardar todos los registros en una sola variable
        resultados = cursor.fetchall()
        # entonces creamos un ciclo for para poder iterar cada uno de ellos
        print('-------------------------------------------------------------------------------------')
        print('                         -> LISTA DE USUARIOS REGISTRADOS <-                         ')
        # aca se va a mostrar de a uno, en un tipo de formato "lista"
        for resultado in resultados:
            print('-------------------------------------------------------------------------------------')
            print(f'{resultado}')
        print('-------------------------------------------------------------------------------------')
