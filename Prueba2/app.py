from flask import Flask, Response, render_template,redirect, url_for, request, get_flashed_messages, flash
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET
from lxml import etree
import os


app = Flask(__name__)

app.secret_key = '1234'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srv_user'
app.config['MYSQL_PASSWORD'] = '4335'
app.config['MYSQL_DB'] = 'Conciertos2'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def generate_xml_data():
    with mysql.connection.cursor() as cursor:
        cursor.callproc("conciertos_artista", (1,))
        info_conciertos = cursor.fetchall()

    root = ET.Element('raiz')
    for row in info_conciertos:
        boleto = ET.SubElement(root, 'boleto')
        nombre_artista = ET.SubElement(boleto, 'nombre_artista')
        nombre_concierto = ET.SubElement(boleto, 'nombre_concierto')
        fecha = ET.SubElement(boleto, 'fecha')
        ubicacion = ET.SubElement(boleto, 'ubicacion')
        nombre_artista.text = row['nombre_artista']
        nombre_concierto.text = row['nombre_concierto']
        fecha.text = str(row['fecha'])
        ubicacion.text = row['ubicacion']

    tree = ET.ElementTree(root)
    return tree

@app.route('/concierto')
def display_xml():
    xml_tree = generate_xml_data()
    xml_string = ET.tostring(xml_tree.getroot(), encoding='utf-8')
    return Response(xml_string, content_type='text/xml')

@app.route('/insert', methods=['GET','POST'])
def insertarConcierto():
    if request.method == 'POST':
        nombre_artista = request.form['nombre_artista']
        nombre_concierto =request.form['nombre_concierto']
        fecha = request.form['fecha']
        ubicacion = request.form['ubicacion']
        genero = request.form['genero']
        
        # Insertamos un nuevo artista primero
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Artistas (nombre_artista,genero) VALUES (%s,%s)", (nombre_artista,genero,))
        mysql.connection.commit()
        
        # Obtenemos el id del artista que acabamos de insertar
        cursor.execute("SELECT idArtista FROM Artistas WHERE nombre_artista = %s", (nombre_artista,))
        id_artista = cursor.fetchone()
        id_artista = id_artista['idArtista']
        
        # Insertamos un nuevo concierto
        cursor.execute("INSERT INTO Conciertos (nombre_concierto, fecha, ubicacion, id_artista) VALUES (%s, %s, %s, %s)", (nombre_concierto, fecha, ubicacion, id_artista))
        mysql.connection.commit()
        cursor.close()
        
        flash('Concierto agregado correctamente')
        
        
        
        return redirect('/insert')
    
    return render_template('formulario.html')
    

@app.route('/concierto/<int:id>')
def display_xml_concierto(id):
    with mysql.connection.cursor() as cursor:
        cursor.callproc("conciertos_artista", (id,))
        info_concierto = cursor.fetchall()

    root = etree.Element('raiz')
    for row in info_concierto:
        boleto = etree.SubElement(root, 'boleto')
        nombre_artista = etree.SubElement(boleto, 'nombre_artista')
        nombre_concierto = etree.SubElement(boleto, 'nombre_concierto')
        fecha = etree.SubElement(boleto, 'fecha')
        ubicacion = etree.SubElement(boleto, 'ubicacion')
        nombre_artista.text = row['nombre_artista']
        nombre_concierto.text = row['nombre_concierto']
        fecha.text = str(row['fecha'])
        ubicacion.text = row['ubicacion']

    tree = etree.ElementTree(root)
    
    arbol_xsl = etree.parse(os.path.join('xsl', 'transformacionC.xsl'))
    transformacion= etree.XSLT(arbol_xsl)
    xml_transformado = transformacion(root)

    return Response(etree.tostring(xml_transformado, encoding='utf-8'), content_type='text/html')
    


if __name__ == '__main__':
    app.run(debug=True)
