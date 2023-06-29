from clases import UsuarioDAO

#La clase Gasto la utilizamos para guardar los gastos suministrados por el usuario en la base de datos

# Constantes de la clase, en este caso utilizaremos 3 consultas SQL que interatuaran con la base de datos:
# _GUARDAR_GASTOS: Es una consulta de inserción que se utiliza para guardar un gasto en la base de datos. Se proporcionan cuatro valores para ser insertados en la tabla "gastos": tipo, descripción, monto y usuario_id.
# _LIMPIAR_GASTOS: Es una consulta de eliminación que se utiliza para borrar todos los registros de la tabla "gastos". Esta consulta eliminará todos los gastos almacenados en la tabla.
# _OBTENER_MONTO_INICIAL: Es una consulta de selección que se utiliza para obtener el valor del campo "monto_inicial" de la tabla "login" para un nombre de usuario específico.
class Gasto:
    _GUARDAR_GASTOS = 'INSERT INTO gastos (tipo, descripcion, monto, usuario_id)' \
                      'VALUES(%s, %s, %s, %s)'
    _LIMPIAR_GASTOS = 'DELETE FROM gastos'
    _OBTENER_MONTO_INICIAL = 'SELECT monto_inicial FROM login WHERE nombre_usuario=%s'



# Creamos un metodo de clase para guardar los datos proporcionados por el usuario de la Clase Casa
    @classmethod

    # Utlizamos los parametros gasto_nuevo(objeto que representa nuevos gastos), cursor, user y user_pass(recuperan
    # informacion del usuario).
    def guardar_gastos_casa(cls, gasto_nuevo, cursor, user, user_pass):
        usuario = cls.obtenerUsuario(user, user_pass, cursor)   #  Le asignamos a la variable el método llamado obtenerUsuario para recuperar la información del usuario
        valores_casa = ('casa', 'alquiler', gasto_nuevo.alquiler, usuario[0])
        # Creamos una tupla que contienen los valores que se insertarán en la tabla de la base de datos.Cada tupla representa
        # un tipo específico de gasto relacionado con una casa(alquiler, servicios, impuestos, alimentos).El formato de cada
        # tupla es(categoría, tipo_de_gasto(casa), monto, id_de_usuario).Usamos[0] para obtener el id_usuario, ya que es la
        # primera posicion en la tupla obtenida a través del 'fecthone' en el método'obtener_usuario'

        cursor.execute(cls._GUARDAR_GASTOS, valores_casa)  # El método cursor.execute  ejecuta la sentencia SQL (cls._GUARDAR_GASTOS) utilizando la tupla valores_casa como parámetros.


        valores_casa = ('casa', 'servicios', gasto_nuevo.servicios, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_casa)

        valores_casa = ('casa', 'impuestos', gasto_nuevo.impuestos, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_casa)

        valores_casa = ('casa', 'alimentos', gasto_nuevo.alimentos, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_casa)

    @classmethod

    # Método de clase para guardar los gastos de la clase Educaión
    # Utlizamos los parametros gasto_nuevo(objeto que representa nuevos gastos), cursor, user y user_pass(recuperan informacion del usuario).
    def guardar_gastos_educacion(cls, gasto_nuevo, cursor, user, user_pass):

        usuario = cls.obtenerUsuario(user, user_pass, cursor)   #  Le asignamos a la variable el método llamado obtenerUsuario para recuperar la información del usuario

        # Creamos una tupla que contienen los valores que se insertarán en la tabla de la base de datos.El formato de cada tupla es(categoría, tipo_de_gasto(gastos escolares), monto, id_de_usuario).Usamos[0]
        # para obtener el id_usuario, ya que es la primera posicion en la tupla obtenida a través del 'fecthone' en el método 'obtener_usuario'
        valores_educacion = ('educacion', 'gastos escolares', gasto_nuevo.monto, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_educacion)   # El método cursor.execute  ejecuta la sentencia SQL (cls._GUARDAR_GASTOS) utilizando la tupla valores_ educación como parámetros.


    @classmethod
    # Método de clase para guardar los gastos de la clase Vehículo
    # Utlizamos los parametros gasto_nuevo(objeto que representa nuevos gastos), cursor, user y user_pass(recuperan
    # informacion del usuario).
    def guardar_gastos_vehiculo(cls, gasto_nuevo, cursor, user, user_pass):
        usuario = cls.obtenerUsuario(user, user_pass, cursor)
        # Creamos una tupla que contienen los valores que se insertarán en la tabla de la base de datos.Cada tupla representa
        # un tipo específico de gasto relacionado con una casa(pantente, combustible, seguro).El formato de cada
        # tupla es(categoría, tipo_de_gasto(vehiculo), monto, id_de_usuario).Usamos[0] para obtener el id_usuario, ya que es la
        # primera posicion en la tupla obtenida a través del 'fecthone' en el método'obtener_usuario'
        valores_vehiculo = ('vehiculo', 'patente', gasto_nuevo.patente, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_vehiculo)   # El método cursor.execute  ejecuta la sentencia SQL (cls._GUARDAR_GASTOS) utilizando la tupla valores_ vehículo como parámetros.

        valores_vehiculo = ('vehiculo', 'combustible', gasto_nuevo.combustible, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_vehiculo)

        valores_vehiculo = ('vehiculo', 'seguro', gasto_nuevo.seguro, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_vehiculo)

    @classmethod
    # Método de clase para guardar los gastos de la clase Tarjeta
    # Utlizamos los parametros gasto_nuevo(objeto que representa nuevos gastos), cursor, user y user_pass(recuperan informacion del usuario).
    def guardar_gastos_tarjeta(cls, gasto_nuevo, cursor, user, user_pass):
        usuario = cls.obtenerUsuario(user, user_pass, cursor) #  Le asignamos a la variable el método llamado obtenerUsuario para recuperar la información del usuario

        # Creamos una tupla que contienen los valores que se insertarán en la tabla de la base de datos.El formato de cada tupla es(categoría, tipo_de_gasto(tarjeta), monto, id_de_usuario).Usamos[0]
        # para obtener el id_usuario, ya que es la primera posicion en la tupla obtenida a través del 'fecthone' en el método 'obtener_usuario'
        valores_tajeta = ('tarjeta', gasto_nuevo.nombre_tarjeta, gasto_nuevo.monto, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_tajeta)  # El método cursor.execute  ejecuta la sentencia SQL (cls._GUARDAR_GASTOS) utilizando la tupla valores_ tarjeta como parámetros.

    @classmethod
    # Método de clase para guardar los gastos de la clase Gastos_varios
    # Utlizamos los parametros gasto_nuevo(objeto que representa nuevos gastos), cursor, user y user_pass(recuperan informacion del usuario).
    def guardar_gastos_varios(cls, gasto_nuevo, cursor, user, user_pass):
        usuario = cls.obtenerUsuario(user, user_pass, cursor) #  Le asignamos a la variable el método llamado obtenerUsuario para recuperar la información del usuario

        # Creamos una tupla que contienen los valores que se insertarán en la tabla de la base de datos.El formato de cada tupla es(categoría, tipo_de_gasto('a completar por el usuario'), monto, id_de_usuario).Usamos[0]
        # para obtener el id_usuario, ya que es la primera posicion en la tupla obtenida a través del 'fecthone' en el método 'obtener_usuario'
        valores_gastos_varios = ('gastos varios', gasto_nuevo.detalle, gasto_nuevo.monto_gastos_varios, usuario[0])
        cursor.execute(cls._GUARDAR_GASTOS, valores_gastos_varios)   # El método cursor.execute  ejecuta la sentencia SQL (cls._GUARDAR_GASTOS) utilizando la tupla valores_ gastos_varios como parámetros.

    @classmethod
    # Método de clase para obtener un usuario
    def obtenerUsuario(cls, usuario_registrado, password_registrado, cursor):  # Este método recibe  tres argumentos: usuario_registrado, password_registrado y cursor

        valores = (usuario_registrado, password_registrado)  # Creamos una tupla que contiene el usuario registrado y el password

        cursor.execute(UsuarioDAO._MOSTRAR_UN_USUARIO, valores)  # Ejecutamos la consulta con la tupla com parámetro

        return cursor.fetchone() # Retornamos el resultado de la consulta a traves de 'fetchone', ya que nos devuelve un registro



    @classmethod
    # Método de clase  para limpiar o eliminar gastos de la base de datos.
    def limpiar_gastos(cls, cursor):
        cursor.execute(cls._LIMPIAR_GASTOS)  # Consulta a la base de datos para limpiar los gastos.

        gastos_eliminados = cursor.rowcount  # Se recupera el número de filas afectadas por la consulta (eliminadas) y lo asignamos a la variable gastos_eliminados.

        print(f'\n- Gastos eliminados con éxito: {gastos_eliminados}')   # Mostramos un mensaje que indica el número de gastos eliminados correctamente.

    @classmethod
    # Método de clase para obtener el monto inicial poroporcionado por el usuario

    def obtener_monto_inicial(cls, usuario_registrado, cursor):   # Utilizamos los parametros usuario_registrado(recuperamos informacion del usuario) y cursor.

        valores = (usuario_registrado,)  # Le asignamos a la variable una tupla que contiene la información del usario.

        cursor.execute(cls._OBTENER_MONTO_INICIAL, valores)  # Ejecutamos la consulta con la tupla como parámetro

        monto_inicial_obtenido = cursor.fetchone()[0]   #Recuperamos el resultado del consulta usando 'fetchone' y [0] para extraer el valor de esa posición

        return int(monto_inicial_obtenido)    # Retornamos como int el resultado obtenido