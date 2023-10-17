
CREATE TABLE Ingredientes (
	idIngrediente INT NOT NULL,
	nombre_ingrediente VARCHAR(50) NOT NULL,
	PRIMARY KEY (idIngrediente)
);


CREATE TABLE Receta (
	idReceta INT NOT NULL,
	nombre_receta VARCHAR(50) NOT NULL,
	PRIMARY KEY (idReceta)
);



CREATE TABLE RecetaIngrediente (
	id_receta INT NOT NULL,
	id_ingrediente INT NOT NULL,
	cantidad INT NOT NULL,
	PRIMARY KEY (id_receta, id_ingrediente),
	FOREIGN KEY (id_ingrediente) REFERENCES Ingredientes(idIngrediente),
	FOREIGN KEY (id_receta) REFERENCES Receta(idReceta)
);


/*Recetas*/

INSERT INTO Receta (idReceta, nombre_receta) VALUES (1, 'Tacos');
INSERT INTO Receta (idReceta, nombre_receta) VALUES (2, 'Torta');
INSERT INTO Receta (idReceta, nombre_receta) VALUES (3, 'Tostadas');

/*Ingredientes*/
INSERT INTO Ingredientes (idIngrediente, nombre_ingrediente) VALUES (1, 'Tortilla');
INSERT INTO Ingredientes (idIngrediente, nombre_ingrediente) VALUES (2, 'Carne');
INSERT INTO Ingredientes (idIngrediente, nombre_ingrediente) VALUES (3, 'Lechuga');
INSERT INTO Ingredientes (idIngrediente, nombre_ingrediente) VALUES (4, 'Pan');
INSERT INTO Ingredientes (idIngrediente, nombre_ingrediente) VALUES (5, 'Milanesa');


/*Ingredientes de cada receta*/
INSERT INTO RecetaIngrediente (id_receta, id_ingrediente, cantidad) VALUES (1, 1, 2);
INSERT INTO RecetaIngrediente (id_receta, id_ingrediente, cantidad) VALUES (2, 5, 3);
INSERT INTO RecetaIngrediente (id_receta, id_ingrediente, cantidad) VALUES (3, 3, 1);



/**/


