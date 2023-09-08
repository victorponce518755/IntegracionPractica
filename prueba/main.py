
from flask import Flask, Response
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srv_user'
app.config['MYSQL_PASSWORD'] = '4335'
app.config['MYSQL_DB'] = 'Servicios'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def generate_xml_data():
    cursor = mysql.connection.cursor()


#en el cursor execute manda a llamar al store procedure llamado dameIngredientes, que recibe un  id de entrada que viene del link
    cursor.execute("CALL dameIngredientes(1)")
    info_Receta = cursor.fetchall()
    


    root = ET.Element('raiz')
    for row in info_Receta:
        ingrediente = ET.SubElement(root, 'ingrediente')
        nombre = ET.SubElement(ingrediente, 'nombre')
        cantidad = ET.SubElement(ingrediente, 'cantidad')
        nombre.text = row['nombre_ingrediente']
        cantidad.text = str(row['cantidad'])


    tree = ET.ElementTree(root)
    return tree

@app.route('/')
def display_xml():
    xml_tree = generate_xml_data()
    xml_string = ET.tostring(xml_tree.getroot(), encoding='utf-8')
    return Response(xml_string, content_type='text/xml')

if __name__ == '__main__':
    app.run(debug=True)
