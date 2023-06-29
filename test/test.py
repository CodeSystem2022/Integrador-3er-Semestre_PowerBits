
# -------------------------------------------------- DOCUMENTACIÓN ----------------------------------------------------
# En este programa, lo que hacemos es el login para la aplicación del gestor de gastos,
# con menu general, menu de usuario y menu de administrador, también está conectado a una base de datos,
# donde se hacen consultas para iniciar sesión, también se pueden guardar nuevos usuarios, pero estos aparecerán
# reflejados en la base de datos una vez que salimos del programa.
from clases.Casa import Casa
from clases.Educacion import Educacion
from clases.Gastos_varios import Gastos_varios
from clases.TarjetadeCredito import TarjetaDeCredito
from clases.UsuarioDAO import UsuarioDAO
from clases.Conexion import Conexion
from clases.Vehiculo import Vehiculo


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

                        # esta opción solo sirve para el ciclo while interno del usuario
                        # ponemos None para que no tenga valor, después una vez que entro al ciclo va a tener el
                        # valor que el usuario le asigne
                        opcion_usuario = None
                        # el ciclo while interno del usuario, va a funcionar mientras la opción sea diferente de 5,
                        # en el momento que sea igual a 5, el ciclo se detiene y vuelve al menu principal
                        while opcion_usuario != 5:
                            try:
                                print('\n     ------ MENU USUARIO ------')
                                print('1- Ver datos de usuario')
                                print('2- Actualizar datos')
                                print('3- Eliminar usuario')
                                print('4- Gestor de gastos')
                                print('5- Salir del menu de usuario')
                                # le pedimos al usuario una opción
                                opcion_usuario = int(input('\n-> Digite una opción de menú: '))
                                # en estos condicionales, según la opción que ingrese el usuario,
                                # es la acción que realiza
                                if opcion_usuario == 1:
                                    # aca con la clase UsuarioDAO y el método mostrar_un_usuario, podemos ver
                                    # los datos que tiene el usuario que ha iniciado sesión, para esto le tenemos
                                    # que pasar los datos del usuario y el cursor para que realice la acción
                                    UsuarioDAO.mostrar_un_usuario(usuario_registrado, password_registrado, cursor)

                                elif opcion_usuario == 2:
                                    print(f'Datos registrados: ') #Mostramos los datos registrados del usuario
                                    UsuarioDAO.mostrar_un_usuario(usuario_registrado, password_registrado, cursor)
                                    print('\n                -- ACTUALIZAR DATOS --') #Ahora comenzamos a pedir los nuevos datos
                                    print('-> Por favor digite: ')
                                    nombre_nuevo = input('- Nombre: ')
                                    apellido_nuevo = input('- Apellido: ')
                                    email_nuevo = input('- Email: ')
                                    monto_inicial_nuevo = int(input('- Ingreso Mensual Nuevo: $'))
                                    nombre_usuario_nuevo = input('- Nombre de Usuario: ')
                                    password_nuevo = input('- Password: ')
                                    # Llamamos al metodo "actualizar_usuario" con sus parametros para poder guardar los nuevos datos del usuario
                                    UsuarioDAO.actualizar_usuario(nombre_nuevo, apellido_nuevo, email_nuevo,
                                                                   monto_inicial_nuevo, nombre_usuario_nuevo,
                                                                   password_nuevo, usuario_registrado, cursor)

                                elif opcion_usuario == 3:
                                    print(f'Datos registrados: ') # Mostramos los datos registrados del usuario
                                    UsuarioDAO.mostrar_un_usuario(usuario_registrado, password_registrado, cursor)
                                    print('\n -- ELIMINAR USUARIO --')
                                    # Llamamos al metodo "eliminar_usuario" para poder eliminar los datos del usuario indicado
                                    UsuarioDAO.eliminar_usuario(usuario_registrado, cursor)

                                elif opcion_usuario == 4:
                                    # Aca comienza el Gestor de gastos donde pedimos que el usuario ingrese sus gastos
                                    print('\n               - - GESTOR DE GASTOS - -')
                                    print('-> En caso de NO tener gasto, ingrese el valor de 0 (cero)...')
                                    # Pedimos que ingrese los gastos de la CASA
                                    print('\n                - - Gastos de casa - -')
                                    print('-> Digite por favor:')
                                    alquiler = float(input('- Alquiler: $'))
                                    servicio = float(input('- Sevicios: $'))
                                    impuestos = float(input('- Impuestos: $'))
                                    alimentos = float(input('- Alimentos: $'))
                                    casa1 = Casa(alquiler, servicio, impuestos, alimentos) # Creamos un objeto de la clase "Casa" donde se van a guardar los datos
                                    # Desde el objeto "casa1" llamamos al metodo "guardar_gastos_casa" donde vamos a guardar los gastos de la Casa ingresados
                                    casa1.guardar_gastos_casa(casa1, cursor, usuario_registrado, password_registrado)
                                    # A la variable "total_global" se le asigna el monto de todos los gastos de la casa, que luego
                                    # se van sumando con los demas gastos
                                    total_global += casa1.monto

                                    print('\n              - -Gastos de educación - -')
                                    # Pedimos que ingrese el gasto de Educacion
                                    print('-> Digite por favor:')
                                    monto = float(input('- Educacion: $'))
                                    educacion1 = Educacion(monto) # Creamos un objeto de la clase "Educacion"
                                    total_global += educacion1.monto # Se le suma el monto de "Educacion" a la variable "total_global"
                                    # Desde el objeto "educacion1" llamamos al metodo "guardar_gastos_educacion" donde vamos a guardar los gastos de Educacion ingresados
                                    educacion1.guardar_gastos_educacion(educacion1, cursor, usuario_registrado,
                                                                        password_registrado)

                                    print('\n              - - Gastos del vehiculo - -')
                                    # Pedimos que ingrese los gastos del vehiculo
                                    print('-> Digite por favor:')
                                    patente = float(input('- Patente: $'))
                                    combustible = float(input('- Cumbustible: $'))
                                    seguro = float(input('- Seguro: $'))
                                    vehiculo1 = Vehiculo(patente, combustible, seguro) # Creamos un objeto de la clase "Vehiculo"
                                    total_global += vehiculo1.monto #Se le suma el monto de "Vehiculo" a la variable "total_global"
                                    # Desde el objeto "vehiculo1" llamamos al metodo "guardar_gastos_vehiculo" donde vamos a guardar los gastos del Vehiculo ingresados
                                    vehiculo1.guardar_gastos_vehiculo(vehiculo1, cursor, usuario_registrado,
                                                                      password_registrado)

                                    print('\n         - - Gastos de la tarjeta de crédito - -')
                                    # Pedimos que ingrese los datos de la tarjeta de credito
                                    print('-> Digite por favor:')
                                    nombre_tarjeta = input('- Nombre de la tarjeta: ')
                                    monto_tarjeta = float(input('- Monto: $'))
                                    tarjeta1 = TarjetaDeCredito(nombre_tarjeta, monto_tarjeta) # Creamos un objeto de la clase "TarjetaDeCredito"
                                    total_global += tarjeta1.monto #Se le suma el monto de "Tarjeta De Credito" a la variable "total_global"
                                    # Desde el objeto "tarjeta1" llamamos al metodo "guardar_gastos_tarjeta" donde vamos a guardar los gastos de la tarjeta de credito ingresados
                                    tarjeta1.guardar_gastos_tarjeta(tarjeta1, cursor, usuario_registrado,
                                                                    password_registrado)

                                    print('\n                 - - Gastos varios - -')
                                    # Pedimos que ingrese sus Gastos Varios
                                    print('-> Digite por favor:')
                                    detalle = input('- Detalle de la compra: ')
                                    monto_gasto_varios = float(input('- Monto: $'))
                                    gastos_varios1 = Gastos_varios(detalle, monto_gasto_varios) # Creamos un objeto de la clase "Gastos_varios"
                                    total_global += gastos_varios1.monto_gastos_varios #Se le suma el monto de "Gastos varios" a la variable "total_global"
                                    # Desde el objeto "tarjeta1" llamamos al metodo "guardar_gastos_tarjeta" donde vamos a guardar los gastos de la tarjeta de credito ingresados
                                    gastos_varios1.guardar_gastos_varios(gastos_varios1, cursor, usuario_registrado,
                                                                         password_registrado)
                except Exception as e:
                    print(f'\n-> Ocurrió un error en el menu principal: {e}')