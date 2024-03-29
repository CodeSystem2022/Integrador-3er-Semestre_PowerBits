
# -------------------------------------------------- DOCUMENTACIÓN ----------------------------------------------------
# En este programa, lo que hacemos es el login para la aplicación del gestor de gastos,
# con menu general, menu de usuario y menu de administrador, también está conectado a una base de datos,
# donde se hacen consultas para iniciar sesión, también se pueden guardar nuevos usuarios, pero estos aparecerán
# reflejados en la base de datos una vez que salimos del programa.
from clases.Casa import Casa
from clases.Educacion import Educacion
from clases.Gastos_varios import Gastos_varios
from clases.TarjetadeCredito import TarjetaDeCredito
from clases.Usuario import Usuario
from clases.UsuarioDAO import UsuarioDAO
from clases.Conexion import Conexion
from clases.Vehiculo import Vehiculo
from clases.Gasto import Gasto


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
                    print('4- Salir del programa y guardar cambios')

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

                                    # una vez que se termina de tomar todos los datos de los gastos, pasamos a la parte del manu de detalle
                                    # donde ingresamos con una bandera = True, para que entre directo al while
                                    bandera = True
                                    while bandera:
                                        # utilizamos un try para atrapar los errores que puedan ocurrir
                                        try:
                                            #mostramos el manu
                                            print('\n    - - Menú de detalle - -')
                                            print('1- Obtener resumen detallado')
                                            print('2- Mostrar monto final')
                                            print('3- Salir del menú de detalle')

                                            opcion_resumen = int(input('\n-> Digite opción: '))

                                            # aca si la opcion = 1, mostramos todos los detalles de los objetos creados,
                                            # con el método mostrar_detalle()
                                            if opcion_resumen == 1:

                                                print(f'\n--------------------------------------------------')
                                                print(f'           RESUMEN DETALLADO DE GASTOS           ')
                                                print(f'--------------------------------------------------')
                                                print(casa1.mostrar_detalle())
                                                print(f'--------------------------------------------------')
                                                print(educacion1.mostrar_detalle())
                                                print(f'--------------------------------------------------')
                                                print(tarjeta1.mostrar_detalle())
                                                print(f'--------------------------------------------------')
                                                print(vehiculo1.mostrar_detalle())
                                                print(f'--------------------------------------------------')
                                                print(gastos_varios1.mostrar_detalles())
                                                print(f'--------------------------------------------------')

                                                # aca obtenemos el monto incial del usuario que ha iniciado sesion,
                                                # esto lo hacemos utilizando el metodo obtener_monto_inicial(), pasandole
                                                # el usuario registrado y el cursor para que pueda hacer la consulta
                                                monto_inicial_obtenido = Gasto.obtener_monto_inicial(usuario_registrado, cursor)
                                                # aca hacemos la resta del monto inicial obtenido y el total de los gastos
                                                resto_sueldo = (monto_inicial_obtenido - total_global)

                                                # luego mostramos en forma de resumen
                                                print(f'\n\n                       RESUMEN                       ')
                                                print(f'-------------------------------------------------')
                                                print(f'- Ingreso mensual registrado  ->   ${monto_inicial_obtenido}')
                                                print(f'- Total del gastos mensuales  ->   ${total_global}')
                                                print(f'                                -----------------')
                                                print(f'- Total resto                 ->   ${resto_sueldo}')
                                                print(f'-------------------------------------------------')

                                            # aca solo mostramos el monto total de los gastos
                                            elif opcion_resumen == 2:
                                                print(f'\n-------------------------------------------------')
                                                print(f'- Monto total de los gastos: ${total_global}')
                                                print(f'-------------------------------------------------')
                                            # si el usuario ingresa 3, la bandera pasa a ser falsa y sale del ciclo
                                            elif opcion_resumen == 3:
                                                bandera = False
                                            # si no ingreso una opcion incorrecta
                                            else:
                                                print('\n-> Opción ingresada no existe')
                                        # esto nos va a decir si tenemos un type error
                                        except Exception as e:
                                            print(f'\n-> Ocurrió un error: {e}')

                                elif opcion_usuario == 5:
                                    print('\n-> Salió del menú de usuario')

                                else:
                                    print('\n-> Opción incorrecta <-')
                            # esto nos va a decir si hay algún error en el menu de usuario
                            except Exception as e:
                                print(f'\n-> Ocurrió un error en el menu de usuario: {e}')

                    elif opcion == 2:

                        print('\n -- USUARIO NUEVO --')
                        print('-> Por favor digite: ')
                        nombre = input('- Nombre: ')
                        apellido = input('- Apellido: ')
                        email = input('- Email: ')
                        monto_inicial = int(input('- Ingreso Inicial: $'))
                        nombre_usuario = input('- Nombre de Usuario: ')
                        password = input('- Password: ')
                        # aca lo mismo que en la opción 1, le pedimos todos los datos al usuario nuevo, y creamos un
                        # objeto de tipo Usuario, pasándole los datos anteriormente pedidos.
                        usuario_nuevo = Usuario(nombre, apellido, email, monto_inicial, nombre_usuario, password)
                        # ahora, con la clase UsuarioDAO y el método agregar_usuario, podremos agregar un usuario nuevo
                        # a la base de datos, para poder realizar esta acción le pasamos al método, el objeto creado y
                        # el cursor.
                        UsuarioDAO.agregar_usuario(usuario_nuevo, cursor)


                    elif opcion == 3:
                        # en esta parte, lo que hicimos fue generar "constantes" con los datos del admin, para poder
                        # iniciar sesión, y que no cualquiera pueda entrar a esta parte
                        _USUARIO_ADMIN = 'admin'
                        _PASSWORD_ADMIN = 'admin'
                        # pedimos los datos para después comprobar si son correctos
                        print('\n-> Esta intentando ingresar como ADMIN, por favor digite: ')
                        usuario_admin = input('- Usuario ADMIN: ')
                        password_admin = input('- Password ADMIN: ')
                        # con esta bandera, vamos a entrar al ciclo while, este va a funcionar hasta que la bandera
                        # tome el valor de falso
                        bandera = True
                        while bandera:
                            # comprobamos si el usuario y el password del admin son iguales a las "constantes"
                            if usuario_admin == _USUARIO_ADMIN and password_admin == _PASSWORD_ADMIN:

                                # esta opción solo sirve para el menu de administrador
                                # ponemos None para que no tenga valor, después una vez que entro al ciclo va a tener
                                # el valor que el usuario le asigne
                                opcion_admin = None

                                # el ciclo while interior, va a funcionar mientras la opción sea diferente de 5,
                                # en el momento que sea igual a 5, el programa sale del menu de administrador y
                                # vuelve al menu principal
                                while opcion_admin != 5:
                                    try:
                                        print('\n     ------ MENU ADMIN ------')
                                        print('1- Ver lista de usuarios')
                                        print('2- Actualizar usuario')
                                        print('3- Limpiar tabla de usuarios')
                                        print('4- Limpiar tabla de gastos')
                                        print('5- Salir del menu de ADMIN')

                                        # le pedimos al usuario una opción
                                        opcion_admin = int(input('\n-> Digite una opción de menú: '))

                                        # en estos condicionales, según la opción que ingrese el usuario,
                                        # es la acción que realiza
                                        if opcion_admin == 1:
                                            # aca con la clase UsuarioDAO y el método mostrar_usuarios, podremos ver en
                                            # consola el listado de los usuarios registrados
                                            # también se le pasa el cursor, para poder realizar la acción
                                            UsuarioDAO.mostrar_usuarios(cursor)

                                        elif opcion_admin == 2:
                                            print(f'\n  - - DATOS REGISTRADOS ANTERIORMENTE - -')
                                            # Llamamos al metodo mostrar_usuarios para que nos muestre los datos del usuario a actualizar.
                                            UsuarioDAO.mostrar_usuarios(cursor)
                                            print('\n            -- ACTUALIZAR DATOS --')
                                            # Acá le pedimos todos los datos al usuario para que los actualice.
                                            print('\n-> Por favor digite: ')
                                            id_usuario_actualizar = int(input('- Id Usuario: '))
                                            nombre_nuevo = input('- Nombre: ')
                                            apellido_nuevo = input('- Apellido: ')
                                            email_nuevo = input('- Email: ')
                                            monto_inicial_nuevo = input('- Ingreso Mensual: $')
                                            nombre_usuario_nuevo = input('- Nombre de Usuario: ')
                                            password_nuevo = input('- Password: ')
                                            # Utilizamos el metodo actualizar_usuario_admin y le pasamos los parámetros de (nombre_nuevo, apellido_nuevo,email_nuevo,
                                            # monto_inicial_nuevo,nombre_usuario_nuevo,password_nuevo,id_usuario_actualizar y cursor)
                                            # para que este actualice los datos del usuario.
                                            UsuarioDAO.actualizar_usuario_admin(nombre_nuevo, apellido_nuevo,
                                                                                 email_nuevo,
                                                                                 monto_inicial_nuevo,
                                                                                 nombre_usuario_nuevo,
                                                                                 password_nuevo, id_usuario_actualizar,
                                                                                 cursor)

                                        elif opcion_admin == 3:
                                        # Ingresamos una bandera = True, para que entre directo al while
                                            bandera = True
                                            while bandera:

                                                # utilizamos un try para atrapar los errores que puedan ocurrir
                                                try:
                                                    # Mostramos una pequeña advertencia sobre si está seguro de querer eliminar todos los usuarios registrados
                                                    print('\n        -- LIMPIAR TABLA DE USUARIOS --')
                                                    print(f'Esta seguro que desea eliminar todos los usuarios: ')
                                                    print('\n 1- Sí')
                                                    print('\n 2- No, deseo volver al menú principal')
                                                    opcion_eliminar_usuarios = int(input('\n-> Digite una opción: '))
                                                    # Si el usuario ingresa "1" se elimnan todos los usuarios
                                                    if opcion_eliminar_usuarios == 1:
                                                        UsuarioDAO.limpiar_usuarios(cursor)
                                                        bandera = False
                                                    # Si el usuario ingresa "2" se vuelve al menú principal
                                                    elif opcion_eliminar_usuarios == 2:
                                                        bandera = False
                                                    else:
                                                        print(f'\n- Opción incorrecta: {opcion_eliminar_usuarios}')
                                                # Esto nos va a decir si hay algún error y el tipo de error dentro del menú de usuario ADMIN
                                                except Exception as e:
                                                    print(f'\n- Ocurrió un error en el menu de usuario ADMIN: {e}')

                                        elif opcion_admin == 4:
                                            # Ingresamos una bandera = True, para que entre directo al while
                                            bandera = True
                                            while bandera:
                                                # Utilizamos un try para poder atrapar los errores sin necesidad de parar el programa
                                                try:
                                                    # En esta opcion lo que se va hacer es limpiar toda la tabla de gastos
                                                    print('\n       -- LIMPIAR TABLA DE GASTOS --')
                                                    # Preguntamos si esta seguro porque una vez borrado no pueden recuperarse los datos
                                                    print(f'Esta seguro que desea eliminar todos los gastos: ')
                                                    print('\n 1- Sí')
                                                    print('\n 2- No, deseo volver al menú principal')
                                                    opcion_eliminar_gastos = int(input('\n->Digite una opción: '))
                                                    # Usamos un if, elif para las opciones que ingrese si quiere eliminar o no los gastos
                                                    if opcion_eliminar_gastos == 1:
                                                        # Llamamos al metodo "limpiar_gastos" de la clase Gasto para limpiar todos los gastos
                                                        Gasto.limpiar_gastos(cursor)
                                                        bandera = False # Si eligio limpiar los datos la bandera cambia su valor a False para que salga del while
                                                    elif opcion_eliminar_gastos == 2:
                                                        bandera = False # Si eligio la opcion 2 la bandera cambia su valor a False y sale del while
                                                    else:
                                                        print(f'\n- Opción incorrecta: {opcion_eliminar_gastos}')# Mostramos la opcion incorrecta ingresada
                                                except Exception as e:
                                                    print(f'\n- Ocurrió un error: {e}') # Mostramos el error si es que ocurrio alguno

                                        elif opcion_admin == 5:
                                            print('\n-> Salio del menu de admin')
                                            # aca cambiamos el valor de la bandera, para que pueda salir el ciclo while
                                            bandera = False

                                        else:
                                            # si el usuario ingresa una opción incorrecta le mostramos un mensaje
                                            print('\n-> Opción Incorrecta <-')

                                    # aca es donde nos va a decir si hay un error o no
                                    except Exception as e:
                                        print(f'\n-> Ocurrió un error en el menu de ADMIN: {e}')
                            # si no son iguales los datos a las "constantes", no va a poder ingresar como admin
                            else:
                                print('\n-> No pudo ingresar como ADMIN...')
                                # colocamos un break para que se termine el ciclo while
                                break

                    elif opcion == 4:
                        # esta parte es del menu principal, si la opción es igual a 4, el programa termina
                        print('\n-> SALIO DEL PROGRAMA, HASTA PRONTO...')

                    # mostramos si ingresa una opción incorrecta
                    else:
                        print('\n-> Opción incorrecta <-')

                except Exception as e:
                    print(f'\n-> Ocurrió un error en el menu principal: {e}')

