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


class UsuarioDAO:
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

    @classmethod
    # a este método le tenemos que pasar los datos del usuario que inicio sesión, y el cursor para realizar la consulta
    def mostrar_un_usuario(cls, usuario_registrado, password_registrado, cursor):
        # creamos la tupla de valores con los datos del usuario
        valores = (usuario_registrado, password_registrado)
        # ejecutamos el cursor con la sentencia _MOSTRAR_UN_USUARIO, para que solo se muestren los datos del usuario que
        # inicio sesión
        cursor.execute(cls._MOSTRAR_UN_USUARIO, valores)
        # creamos una variable para almacenar la fila que se "afectó" al momento de realizar la consulta, que en este
        # caso sería la que contiene los datos del usuario que inicio sesión
        resultado = cursor.fetchall()
        # y mostramos los datos
        print('--------------------------------------------------------------------------------------------------')
        print('                                      -> DATOS DE USUARIO <-                                      ')
        print('\n- id_usuario / Nombre / Apellido / Email / Ingreso Mensual / Nombre Usuario / Password')
        print(resultado)
        print('--------------------------------------------------------------------------------------------------')

    @classmethod
    # Método para actualizar datos del usuario, recibe los siguientes parametros nombre_nuevo, apellido_nuevo, email_nuevo,
    # monto_inicial_nuevo, nombre_usuario_nuevo, password_nuevo, usuario_registrado y cursor
    def actualizar_usuario(cls, nombre_nuevo, apellido_nuevo, email_nuevo, monto_inicial_nuevo, nombre_usuario_nuevo,
                           password_nuevo, usuario_registrado, cursor):
        valores = (nombre_nuevo,   # Creamos una tupla llamada valores que contiene los nuevos valores del usuario.
                   apellido_nuevo,
                   email_nuevo,
                   monto_inicial_nuevo,
                   nombre_usuario_nuevo,
                   password_nuevo,
                   usuario_registrado
                   )
        cursor.execute(cls._ACTUALIZAR_USUARIO, valores)  # Ejecutamos la consulta y creamos una variable de clase

        usuario_actualizado = cursor.rowcount  # recupera el número de filas afectadas por la operación de actualización
                                               # en la base de datos y lo asigna a la variable usuario_actualizado.

        print(f'\n- Usuario Actualizado con éxito: {usuario_actualizado}') # Mostramos un mensaje que indica la cantidad de usuarios actualizados con éxito.

    @classmethod
    # Creamos el método eliminar usuario
    def eliminar_usuario(cls, usuario_registrado, cursor): #Agregamos los parametos necesarios
        valores = (usuario_registrado,) #Tupla de valores que contiene los datos del usuario
        cursor.execute(cls._ELIMINAR_USUARIO, valores) #Se ejecuta el cursor con la sentencia para eliminar el usuario y la tupla de valores
        usuario_eliminado = cursor.rowcount #almacena la cantidad de usuarios que fueron eliminados de la base de datos
                                            # y los asigna a la variable usuario_eliminado
        print(f'\n- Usuario eliminado con éxito: {usuario_eliminado}') #Mostramos el usuario eliminado

    @classmethod
    # Creamos el método actualizar usuario pero en este caso para la función de ADMIN, que recibe los siguientes parametros:
    # nombre_nuevo, apellido_nuevo, email_nuevo, monto_inicial_nuevo,
    # nombre_usuario_nuevo, password_nuevo, id_usuario_actualizar y cursor.
    def actualizar_usuario_admin(cls, nombre_nuevo, apellido_nuevo, email_nuevo, monto_inicial_nuevo,
                                 nombre_usuario_nuevo,
                                 password_nuevo, id_usuario_actualizar, cursor):
        # ahora, para poder crear la tupla con los valores que necesita la sentencia de _ACTUALIZAR_USUARIO_ADMIN,
        # tenemos que acceder a cada atributo del objeto por separado.
        valores = (nombre_nuevo,
                   apellido_nuevo,
                   email_nuevo,
                   monto_inicial_nuevo,
                   nombre_usuario_nuevo,
                   password_nuevo,
                   id_usuario_actualizar
                   )
        # De esta forma podremos ejecutar la acción del cursor junto con los valores necesarios
        cursor.execute(cls._ACTUALIZAR_USUARIO_ADMIN, valores)
        usuario_actualizado = cursor.rowcount # Recupera el número de filas afectadas por la operación de actualización
                                              # dentro de la base de datos y lo asigna a la variable usuario_actualizado.
        print(f'\n- Usuario Actualizado con éxito: {usuario_actualizado}') # Muestra un mensaje con la cantidad de usuarios actualizados.

    @classmethod
    # Creamos el método para eliminar todos los usuarios
    def limpiar_usuarios(cls, cursor): # Pasamos el cursor como parametro
        cursor.execute(cls._LIMPIAR_USUARIOS) # Se ejecuta el cursor con la sentencia para eliminar los usuarios
        usuarios_eliminados = cursor.rowcount # almacena la cantidad de usuarios que fueron eliminados de la base de datos
                                            # y los asigna a la variable usuarios_eliminados
        print(f'\n- Usuarios eliminados con éxito: {usuarios_eliminados}')