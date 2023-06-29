
import psycopg2 as bd

import sys

class Conexion:
    _DATABASE = 'postgres'
    _USERNAME = 'powerbits'
    _PASSWORD = 'powerbits'
    _DB_PORT = '5432'
    _HOST = 'powerbits-db.c90rmfzu15yz.us-east-1.rds.amazonaws.com'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                print(f"Conexión Exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                print(f'Ocurrio un error de tipo: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrio un error de tipo: {e}')
                sys.exit()
        else:
            return cls._cursor
        
        