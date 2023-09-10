/*
En tu base de datos de boletos para conciertos, has creado una tabla llamada Conciertos que almacena información sobre los conciertos, incluyendo el nombre del concierto, la fecha y la ubicación. Además, en la misma tabla, has incluido campos para el nombre del artista y el género musical. Este diseño puede llevar a la redundancia de datos, ya que un artista puede tener varios conciertos, lo que resulta en información repetida en la base de datos.

Te pediré que realices las consultas correspondientes para obtener recetas y boletos de un producto específico y luego generar el XML correspondiente a través de una aplicación en Flask.

Para resolver este problema, puedes normalizar la base de datos y crear una tabla separada llamada Artistas para almacenar información sobre los artistas. Luego, en la tabla Conciertos, puedes utilizar una clave foránea para referenciar el id_artista en lugar de almacenar el nombre del artista directamente. Esto evitará la redundancia de datos. Para obtener información sobre los conciertos de un artista específico. de nuevo, estas consultas te permitirán obtener la información necesaria para construir el XML correspondiente en tu aplicación Flask.  Luego, en tu aplicación Flask, puedes generar el XML utilizando una biblioteca como lxml o xml.etree.ElementTree y proporcionar el XML en la respuesta HTTP.
*/


CREATE TABLE Artistas (
	idArtista INT NOT NULL AUTO_INCREMENT,
	nombre_artista VARCHAR(50) NOT NULL,
	genero VARCHAR(50) NOT NULL,
	PRIMARY KEY (idArtista)
);

CREATE TABLE Conciertos (
	idConcierto INT NOT NULL AUTO_INCREMENT,
	nombre_concierto VARCHAR(50) NOT NULL,
	fecha DATE NOT NULL,
	ubicacion VARCHAR(50) NOT NULL,
	id_artista INT NOT NULL,
	PRIMARY KEY (idConcierto),
	FOREIGN KEY (id_artista) REFERENCES Artistas(idArtista)
);

/*Artistas*/
INSERT INTO Artistas (idArtista, nombre_artista, genero) VALUES (1, 'Nirvana', 'Melancolica 2');
INSERT INTO Artistas (idArtista, nombre_artista, genero) VALUES (2, 'Morat', 'Melancolica');
INSERT INTO Artistas (idArtista, nombre_artista, genero) VALUES (3, 'The Rock', 'Rock');
INSERT INTO Artistas (idArtista, nombre_artista, genero) VALUES (4, 'The Killers', 'Rock');
INSERT INTO Artistas (idArtista, nombre_artista, genero) VALUES (5, 'Metallica', 'Rock');
INSERT INTO Artistas (idArtista, nombre_artista, genero) VALUES (6, 'Elvis Presley', 'Rock');

/*Conciertos*/
INSERT INTO Conciertos (idConcierto, nombre_concierto, fecha, ubicacion, id_artista) VALUES (1, 'Nirvana en el BBVA', '2017-03-01', 'Estadio BBVA', 1);
INSERT INTO Conciertos (idConcierto, nombre_concierto, fecha, ubicacion, id_artista) VALUES (2, 'Morat y los Tusos', '2017-03-02', 'Nemezio Diez', 2);
INSERT INTO Conciertos (idConcierto, nombre_concierto, fecha, ubicacion, id_artista) VALUES (3, 'Volcan Rock', '2017-03-03', 'EL VOLCAN', 3);
INSERT INTO Conciertos (idConcierto, nombre_concierto, fecha, ubicacion, id_artista) VALUES (4, 'Tighres Metalicos', '2020-03-04', 'Nuevo Estadio Tigres', 4);
INSERT INTO Conciertos (idConcierto, nombre_concierto, fecha, ubicacion, id_artista) VALUES (5, 'Elvis Nou', '2007-10-05', 'Camp Nou', 5);


/*

Dame un stored procedure que reciba el id de un artista y regrese el nombre del artista y los conciertos que tiene en la base de datos.
*/

DELIMITER $$
CREATE PROCEDURE conciertos_artista (IN id_artista INT)
BEGIN
	SELECT nombre_artista, nombre_concierto, fecha, ubicacion FROM Conciertos JOIN Artistas ON Conciertos.id_artista = Artistas.idArtista WHERE Artistas.idArtista = id_artista;
END $$
DELIMITER ;

CALL conciertos_artista(1);

