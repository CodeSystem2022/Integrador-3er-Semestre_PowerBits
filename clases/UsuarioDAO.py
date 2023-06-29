
class UsuarioDAO2:
    
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
   
    def iniciar_sesion(cls, usuario_registrado, password_registrado, cursor):
        
        valores = (usuario_registrado, password_registrado)
        
        cursor.execute(cls._INICIAR_SESION, valores)
        
        resultados = cursor.fetchall()
        
        return resultados
