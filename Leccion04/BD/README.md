# Python

## fetchall y fetchone para conectar py con BD postgress

### fetchone() y fetchall() también son métodos utilizados en Python para obtener resultados de una consulta realizada en una base de datos mediante el uso de la biblioteca psycopg2, que es un adaptador de base de datos PostgreSQL para Python.

## fetchone() 
### se utiliza para recuperar la siguiente fila de un conjunto de resultados y devuelve una tupla. Si no hay más filas disponibles, devuelve None. Por lo tanto, se puede usar fetchone() en un bucle para recuperar todas las filas de un conjunto de resultados.

### Por ejemplo, el siguiente código de Python utiliza fetchone() para obtener la primera fila de un conjunto de resultados:

#### import psycopg2

#### conn = psycopg2.connect(host="myhost", database="mydb", user="myuser", password="mypassword")
#### cur = conn.cursor()

#### cur.execute("SELECT * FROM mi_tabla")
#### fila = cur.fetchone()

#### print(fila)

## fetchall() 
### se utiliza para recuperar todas las filas de un conjunto de resultados y devuelve una lista de tuplas. Si no hay ninguna fila disponible, devuelve una lista vacía. Tenga en cuenta que si el conjunto de resultados es muy grande, usar fetchall() puede consumir una gran cantidad de memoria.

### Por ejemplo, el siguiente código de Python utiliza fetchall() para obtener todas las filas de un conjunto de resultados:

#### import psycopg2

#### conn = psycopg2.connect(host="myhost", database="mydb", user="myuser", password="mypassword")
#### cur = conn.cursor()

#### cur.execute("SELECT * FROM mi_tabla")
#### filas = cur.fetchall()

### Es importante tener en cuenta que tanto fetchone() como fetchall() deben usarse después de ejecutar una consulta con execute().

## Transaccion : Es cuando queremos ejecutar varias consultas sobre lo que es la bd.
### estas consultas van a modificar el estado de la bd ,por ej: colocar un INSERT, UPDATE, DELETE. Todos estos query deben ejecutarse exitosamente, si resulta asi lo commiteamos. si alguno falla debemoes realizar un rollback (dar marcha atras)
for fila in filas:
    print(fila)

