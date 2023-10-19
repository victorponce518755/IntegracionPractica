<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<head>
				<title>Concierto</title>
				<meta charset="utf-8"/>
				<style>
					body{
					background-color: #64B5F6;
					font-family: Arial;
					font-size: 20px;
					text-align: center;
					margin: 0; 
					padding: 0; 
					}
					h1{
					color: #007bff;
					margin-top: 20px;
					}
					h2{
					color: #8D6E63;
					margin : 10px 0;
					}
					p{
					color: #555;
					margin: 5px 0;
					}
					.blanco{
					background-color: #fff;
					padding: 10px;
					margin: 10px;
					border-radius: 5px;
					box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
					}
				</style>
				<link rel="stylesheet" type="text/css" href="css/estilo.css"/>
			</head>
				<body>
					<h1>Felicidades vas al Concierto</h1>
					<xsl:for-each select="raiz/boleto">
						<h2>Nombre Concierto:<xsl:value-of select="nombre_concierto"/></h2>
						<div class="blanco">
							<p>
								Nombre Artista: <xsl:value-of select="nombre_artista"/>
							</p>
							<p>
								Fecha: <xsl:value-of select="fecha"/>
							</p>
							<p>
								Ubicacion:<xsl:value-of select="ubicacion"/>
							</p>
							<h2>
								TicketMaster
							</h2>
						</div>
						
					</xsl:for-each>
				</body>	
		</html>	
	</xsl:template>
</xsl:stylesheet>