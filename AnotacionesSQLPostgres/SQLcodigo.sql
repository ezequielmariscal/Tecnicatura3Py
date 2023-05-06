--como consultar en mi querytools de pg?
SELECT * FROM persona WHERE id_persona = 1
--o tambien asi
SELECT * FROM persona WHERE id_persona in (1,2)
--como comentamos??
-- (usamos 2 guias)
--como insertamos mas cosas al registro en persona?
INSERT INTO persona(nombre, apellido, email)VALUES ('Susana', 'Lara', 'slara@mail.com')
--como modficar un registro? (no olvidar el where que es el filtro para saber que queremos borrar)
UPDATE persona SET nombre = 'Ivonne', apellido = 'Esparza', email = 'iesparza@mail.com' WHERE id_persona = 3
--como elimino todo?(its pegriloso!)
DELETE FROM persona
--como borrar algo en especifico?
DELETE FROM persona WHERE id_persona = 3