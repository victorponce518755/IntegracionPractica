from flask import Flask, Response, render_template,redirect, url_for, request, get_flashed_messages, flash
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET

app = Flask(__name__)

app.secret_key = '1234'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srv_user'
app.config['MYSQL_PASSWORD'] = '4335'
app.config['MYSQL_DB'] = 'Servicios2'
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

@app.route('/receta')
def display_xml():
    xml_tree = generate_xml_data()
    xml_string = ET.tostring(xml_tree.getroot(), encoding='utf-8')
    return Response(xml_string, content_type='text/xml')


#########Nos falta modificar las queries para que hagan todo de un jalon, ademas checar que este bien el nombre de los campos de la tabla######
@app.route('/insertar', methods=['GET','POST'])
def insertarIngrediente():
    if request.method == 'POST':
        nombre_receta = request.form['nombre_receta']
        nombre_ingrediente =request.form['nombre_ingrediente']
        cantidad = request.form['cantidad']
        
        #Insertamos un nuevo ingrediente primero
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Ingredientes (nombre_ingrediente) VALUES (%s)", (nombre_ingrediente,))
        mysql.connection.commit()
        
        #Obtenemos el id del ingrediente que acabamos de insertar
        cursor.execute("SELECT idIngrediente FROM Ingredientes WHERE nombre_ingrediente = %s", (nombre_ingrediente,))
        id_ingrediente = cursor.fetchone()
        id_ingrediente = id_ingrediente['idIngrediente']
        
        
        #Insertammos la nueva receta a la tabla de recetas
        cursor.execute("INSERT INTO Receta (nombre_receta) VALUES (%s)", (nombre_receta,))
        mysql.connection.commit()
        
        #Obtenemos el id de la receta que acabamos de insertar
        cursor.execute("SELECT idReceta FROM Receta WHERE nombre_receta = %s", (nombre_receta,))
        id_receta = cursor.fetchone()
        id_receta = id_receta['idReceta']
        

        #Insertamos las relaciones en la tabla de RecetaIngrediente
        cursor.execute("INSERT INTO RecetaIngrediente (id_receta, id_ingrediente, cantidad) VALUES (%s, %s, %s)", (id_receta, id_ingrediente, cantidad))
        mysql.connection.commit()

        cursor.close()

        flash('Ingrediente agregado correctamente','success')
        
        return redirect('/insertar')
    
    return render_template('formularioInsertar.html', messages=get_flashed_messages())


#Esta es una ruta que nos regresa la informacion de la RecetaIngrediente, es decir del id que le pasemos, nos regresa el nombre del ingrediente, la cantidad y el nombre de la receta

@app.route('/recetaIngrediente/<string:id>')
def recetaIngrediente(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Receta.nombre_receta, Ingredientes.nombre_ingrediente, RecetaIngrediente.cantidad FROM RecetaIngrediente INNER JOIN Receta ON RecetaIngrediente.id_receta = Receta.idReceta INNER JOIN Ingredientes ON RecetaIngrediente.id_ingrediente = Ingredientes.idIngrediente WHERE RecetaIngrediente.id_receta = %s", (id,))
    info_RecetaIngrediente = cursor.fetchall()
    
    cursor.close()
    
    
    print(info_RecetaIngrediente)
    
    return render_template('recetaIngrediente.html', recetaIngrediente = info_RecetaIngrediente)


if __name__ == '__main__':
    app.run(debug=True)
