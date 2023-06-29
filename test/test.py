
# -------------------------------------------------- DOCUMENTACIÓN ----------------------------------------------------
# En este programa, lo que hacemos es el login para la aplicación del gestor de gastos,
# con menu general, menu de usuario y menu de administrador, también está conectado a una base de datos,
# donde se hacen consultas para iniciar sesión, también se pueden guardar nuevos usuarios, pero estos aparecerán
# reflejados en la base de datos una vez que salimos del programa.
from clases.UsuarioDAO import UsuarioDAO
from clases.Conexion import Conexion


class Main:

    total_global = 0
    # Nos conectamos con la base de datos, de forma general
    with Conexion.obtenerConexion():
        with Conexion.obtenerCursor() as cursor:

            # esta opción es para el ciclo while exterior, solo sirve para el menu principal
            # ponemos None para que no tenga valor, después una vez que entro al ciclo va a tener el valor que el
            # usuario le asigne

            opcion = None

            # el ciclo while exterior, va a funcionar mientras la opción sea diferente de 4, en el momento que sea
            # igual a 4, el programa se detiene y ahi recién se van a ver los cambios en la base de datos
            while opcion != 4:
                try:
                    print('\n        ------ MENU ------')
                    print('1- Iniciar sesión')
                    print('2- Usuario nuevo')
                    print('3- Ingresar como ADMIN')
                    print('4- Salir del programa')

                    # le pedimos al usuario que digite una opción
                    opcion = int(input('\n-> Digite una opción de menú: '))

                    # en estos condicionales, según la opción que ingrese el usuario, es la acción que realiza
                    if opcion == 1:
                        bandera = True
                        while bandera:
                            print('\n -- INICIAR SESIÓN --')
                            # usamos dos variables para tomar los datos del usuario que está intentando iniciar sesión
                            usuario_registrado = input('- Usuario: ')
                            password_registrado = input('- Password: ')
                            # usando la clase UsuarioDAO y el método iniciar_sesión, vamos a poder ver si el usuario está
                            # registrado o no, pero para esto vamos a tener que pasarle las variables creadas para que
                            # compruebe lo anteriormente dicho, también le tenemos que pasar el cursor para que pueda
                            # realizar la acción
                            resultados = UsuarioDAO.iniciar_sesion(usuario_registrado, password_registrado, cursor)

                            # Si la comprobación del usuario y contraseña es correcta le muestra un mensaje de bienvenida
                            # donde le muestra el nombre de usuario
                            if len(resultados) > 0:
                                print(f"\n - Inicio de sesión exitoso -> Bienvenido {usuario_registrado} <-")
                                bandera = False

                            # si la comprobación es incorrecta te muestra un mensaje donde te dice que es incorrecto los datos
                            # y te muestra de nuevo el menu para iniciar sesión
                            else:
                                print(
                                    f'\n - Usuario y/o contraseña [{usuario_registrado} / {password_registrado}] incorrecto, inténtelo de nuevo...')
                except Exception as e:
                    print(f'\n-> Ocurrió un error en el menu principal: {e}')