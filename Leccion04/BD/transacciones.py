import psycopg2 as bd
# Esto es para poder conectarnos a Postgres

conexion = bd.connect(  # Creamos objeto Tipo conexion para hacer la conexion
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    conexion.autocommit = False  # lo hacemos para que no se guarden los cambios automaticamente
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    print('Termina la transaccion')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
   conexion.close()