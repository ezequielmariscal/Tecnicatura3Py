# 6 - Clase de excepciones personalizadas
class NumerosIgualesException (Exception): # Extiende de la clase
    def __init__(self,mensaje):
        self.message = mensaje #buscar en el file manejo_excepciones.py line 53