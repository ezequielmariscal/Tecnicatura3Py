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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'  # Placeholder
            entrada = input('Digite los id_person a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)  # tupla de tuplas -- split : separa con coma los element
            cursor.execute(sentencia, llaves_primarias)   # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()   # fetchall= recupera todas las sentencias de registro que seria una list
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
   conexion.close()