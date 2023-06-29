#-------------------------------------- DOCUMENTACION -----------------------------------------------
# En esta clase lo que hacemos es la obtención de la conexión y el cursor, para poder 
# conectarnos a la base de datos y asi poder manipular la misma y hacer consultas.

# esta libreria (psycopg2) nos ayuda a hacer la conexion con la base de datos, hacer consultas, etc.
import psycopg2 as bd

# esta libreria (sys) se utiliza para varias cosas, pero en esta caso la utilizamos para salir 
# del programa si se cumple una condicion
import sys

# creamos la clase Conexion, con todos los datos de la bd, para luego poder 
# establecer una conexion exitosa
class Conexion:
    _DATABASE = 'postgres'
    _USERNAME = 'powerbits'
    _PASSWORD = 'powerbits'
    _DB_PORT = '5432'
    # el host es donde esta alojada nuestra base de datos, en este caso esta en AWS (amazonaws)
    _HOST = 'powerbits-db.c90rmfzu15yz.us-east-1.rds.amazonaws.com'
    # creamos variables que no tienen asignado nada, pero despues utilizarlas al momento
    # de crear la conexion y el cursor
    _conexion = None
    _cursor = None

    # en este metodo lo que hacemos es obtener la conexion a la bd
    @classmethod
    def obtenerConexion(cls):
        # usando un condicional if, decimos que si la conexion es None (anteriormente asiganado) va a entrar
        # al primer bloque de codigo, donde;
        if cls._conexion is None:
            # usamos un try - except para atrapar cualquier error que pueda ocurrir, y que no se pare el programa
            try:
                # entonces, a la variable conexion le asignamos todos los datos de la bd, utilizando "bd.connect"
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                # mostramos un mensaje que fue exitosa la conexion
                print(f"Conexión Exitosa: {cls._conexion}")
                # y por ultimo se retorna la conexion ya lista para utilizarse
                return cls._conexion
            # aca nos va a decir si ocurrio un error dentro del bloque try
            except Exception as e:
                print(f'Ocurrio un error de tipo: {e}')
                # si hay error, lo que hacemos es finalizar la conexion 
                sys.exit()
        # si el programa entra a este bloque de codigo, quiere decir que que la variable conexion no es None,
        # osea que ya existe una conexion, entonces retorna la ya creada
        else:
            return cls._conexion

    # en este metodo obtenemos el cursor
    @classmethod
    def obtenerCursor(cls):
        # si el cursor es None, entra al primer bloque de codigo y lo crea
        if cls._cursor is None:
            # utilizamos un try - except para los error
            try:
                # ahora creamos el cursor, para poder hacer las consultas
                cls._cursor = cls.obtenerConexion().cursor()
                # mostramos que fue creado con exito
                print(f'Se abrio correctamente el cursor: {cls._cursor}')
                # y lo retornamos
                return cls._cursor
            # aca nos dice si hay error
            except Exception as e:
                print(f'Ocurrio un error de tipo: {e}')
                # y salimos
                sys.exit()
        # si entra aca, es porque ya existe un cursor, y retorna ese mismo
        else:
            return cls._cursor
        
        