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
    #  conexion.autocommit = False  # lo hacemos para que no se guarden los cambios automaticamente # Poner autocommit true es mala practica # esto direcatamente no deberia estar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  # Hacemos el commit manualmente
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()  # Lo hacemos para que el commit vuelva para atras y no quede nada en la bd
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
   conexion.close()