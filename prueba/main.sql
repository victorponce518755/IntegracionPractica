CREATE DATABASE Receta;

USE DATABASE Receta;



/*
Stored procedure
*/

DELIMITER $$
CREATE PROCEDURE dameIngredientes (IN idReceta INT)
BEGIN
	SELECT nombre_ingrediente, cantidad FROM RecetaIngrediente JOIN Ingredientes ON RecetaIngrediente.id_ingrediente = Ingredientes.idIngrediente WHERE id_receta = idReceta;
END$$
DELIMITER ;

CALL dameIngredientes(1);
