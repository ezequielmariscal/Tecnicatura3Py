# letra 'r'
archivo = open('prueba.txt', 'r', encoding='utf8') #abro el txt
# print(archivo.read()) # y lo leo con read
# print(archivo.read(5)) # muestra las 1ro 5 letras de la palabra
# print(archivo.read(10))
#print(archivo.readline(10)) # lee las primeras 10 de letras de la 1era linea del txt

# letra 'a' (sirve para anexar la informacion)
# archivo = open('prueba.txt', 'a', encoding='utf8')

# letra 'x' (sirve para crear un archivo)

# como busco un archivo que no se localiza en nuestro arhivos cercanos de python?
# archivo = open('c:\\Users\\zequi\\Universidad\\Tecnicatura3Py\\Archivos\\Leccion02\venv\\Scripts\\python.exeUTNprueba.txt', 'r', encoding='utf8')
# vamos a iterar el archivo, cada una de las lineas
# for linea in archivo:
     # print(linea)  # iteramos todos los elementos del archivo
     # print(archivo.readlines()[11]) # muestra todo como una lista

# Anexamos informacion, copiamos a otro
try:
    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())

finally:
    archivo.close()  # cerramos el primer archivo
    archivo2.close()  # cerramos el segundo archivo



print('Se ha terminado el proceso de leer y copiar archivos')
