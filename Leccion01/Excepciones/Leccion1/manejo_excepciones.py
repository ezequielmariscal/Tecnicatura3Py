# 1 - Ejemplo de excepciones literales
try:
    10/0
except Exception as c:
    print(f'Ocurrio un error: {c}')  # capturamos la excepcion con una clase padre

# 2 -Creamos variables para poder utilizar las expeciones
resultado = None  # la var no tiene valor
a = 10
b = 0
try:
    resultado = a / b  # modificamos para obtener otras expresiones
except Exception as d:  # d es una var que podemos otorgarle el nombre que queramos
    print(f'Ocurrio un error: {d}')

print(f'el resultado es: {resultado}')
print('seguimos...')

# 3 -Como procesar exception mas especificas? ej: pd: si trbjmos con excepciones el var casi siempre va a ser la letra e
resultado = None
a = 10
b = 0
try:
    resultado = a / b  # modificamos para obtener otras expresiones
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')  # type es para saber el tipo
except ZeroDivisionError as e:  # le otorgamos a var (e) una exception especifica
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:  # planteo una exception padre por si la especifica no funciona
    print(f'Exception - Ocurrio un error: {type(e)}')

print(f'el resultado es: {resultado}')
print('seguimos...')

# 4 - Como hacer que mis variables adentro del try es decir que va a ser parte de mi try pero agregando nosotros los nro
resultado = None  # Dejo la var resultado q me sirve para ver mejor c/u de las pruebas

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    resultado = a / b  # modificamos para obtener otras expresiones
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:  # le otorgamos a var (e) una exception especifica
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:  # planteo una exception padre por si la especifica no funciona
    print(f'Exception - Ocurrio un error: {type(e)}')

print(f'el resultado es: {resultado}')
print('seguimos...')

# 5 - Ejecutamos else (sino se ejecuta ningun bloque convocado) y agregamos un finally (sirve para finalizar un recurso)
from NumerosIgualesException import NumerosIgualesException
resultado = None  # Dejo la var resultado q me sirve para ver mejor c/u de las pruebas

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise NumerosIgualesException('Son numeros iguales')
    resultado = a / b  # modificamos para obtener otras expresiones
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:  # le otorgamos a var (e) una exception especifica
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:  # planteo una exception padre por si la especifica no funciona
    print(f'Exception - Ocurrio un error: {type(e)}')
else:
    print(f'No se arrojo ninguna excepcion')
finally:  # Nos sirve para liberar algun recurso
    print('Ejecucion de este bloque final')

print(f'el resultado es: {resultado}')
print('seguimos...')

