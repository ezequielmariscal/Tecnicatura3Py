class PersonaDAO:
    """
    DAO significa : Dara Access Object
    CRUD significa:
                    Create -> Insertar
                    Read   -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apelliodo=%s, email=%s WHERE ID_PERSONA=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'