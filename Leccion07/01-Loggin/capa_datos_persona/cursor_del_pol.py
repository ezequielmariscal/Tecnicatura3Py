from logger_base import log
from conexion import Conexion


class CursorDelPool:
    def __int__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exception, valor_exception, detalle):
        log.debug('Se ejecuta el metodo exit')
        if valor_exception:
            self._conexion.rollback() # vuelve al estado anterior
            log.debug(f'Ocurrio una excepcion: {valor_exception}' )
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchAll())