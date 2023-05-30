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
        with conexion.cursor() as cursor:  # Definimos la sentenciacursor.execute(sentencia)
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Placeholder
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona,))  # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone()  # fetchall= recupera todas las sentencias de registro que seria una list
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
   conexion.close()


# https://www.psycopg.org/docs/usage.html siempre que abrimos una conexion a una base de datos debemos enbolberlo
# en la base de datos xq siempre que se habre hay q finalizarlo

