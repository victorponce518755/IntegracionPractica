
from flask import Flask, Response
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srv_user'
app.config['MYSQL_PASSWORD'] = '4335'
app.config['MYSQL_DB'] = 'Conciertos'
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

if __name__ == '__main__':
    app.run(debug=True)
