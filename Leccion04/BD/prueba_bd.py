import psycopg2
# Esto es para poder conectarnos a Postgres

conexion = psycopg2.connect(  # Creamos objeto Tipo conexion para hacer la conexion
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'  # Definimos la sentencia
cursor.execute(sentencia)  # De esta manera ejecutamos la sentencia
registros = cursor.fetchall()  # fetchall= recupera todas las sentencias de registro que seria una list
print(registros)

cursor.close()
conexion.close()

