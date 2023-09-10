

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



/*Stored Procedures*/
DELIMITER $$
CREATE PROCEDURE conciertos_artista (IN id_artista INT)
BEGIN
	SELECT nombre_artista, nombre_concierto, fecha, ubicacion FROM Conciertos JOIN Artistas ON Conciertos.id_artista = Artistas.idArtista WHERE Artistas.idArtista = id_artista;
END $$
DELIMITER ;

CALL conciertos_artista(1);

