<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<head>
				<title>Receta</title>
				<meta charset="utf-8"/>
				<link rel="stylesheet" type="text/css" href="css/estilo.css"/>
			</head>
			<body>
				<h1>Tu receta</h1>
				<xsl:for-each select="raiz/receta">
					<h2>
						Nombre de la Receta:<xsl:value-of select="nombre_receta"/>
					</h2>
					<div class="blanco">
						<p>
							Nombre del ingrediente: <xsl:value-of select="nombre_ingrediente"/>
						</p>
						<p>
							Cantidad: <xsl:value-of select="cantidad"/>
						</p>
						<h2>
							Tacos Don Lalo
						</h2>
					</div>

				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>