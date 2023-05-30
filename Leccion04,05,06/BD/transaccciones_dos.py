import psycopg2 as bd  # Esto es para poder conectarnos a Postgres

conexion = bd.connect(  # Creamos objeto Tipo conexion para hacer la conexion
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    #  conexion.autocommit = False   # esto direcatamente no deberia estar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Jorge', 'Prol', 'jprol@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Perez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()  # Hacemos el commit manualmente

    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()  # Lo hacemos para que el commit vuelva para atras y no quede nada en la bd
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
   conexion.close()