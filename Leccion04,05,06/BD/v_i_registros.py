# como insertar varios registros

import psycopg2
# Esto es para poder conectarnos a Postgres

conexion = psycopg2.connect(  # Creamos objeto Tipo conexion para hacer la conexion
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Marcos', 'Canto', 'mcanto@mail.com'),
                ('Marcelo', 'Cuenca', 'cuenca@mail.com')
            )  # es una TUPLA de TUPLAS
            cursor.executemany(sentencia, valores)   # De esta manera ejecutamos la sentencia
            # conexion.commit()   esto se utiliza para guardar los cambios de BD no nos hace falta
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
   conexion.close()