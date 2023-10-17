###servicios xml y rest

###servicios xml y rest

from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_socketio import SocketIO

app= Flask(__name__)

#####
#Configuracion de la BD
#####

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srv_user'
app.config['MYSQL_PASSWORD'] = '4335'
app.config['MYSQL_DB'] = 'Servicios'.

mysql= MySQL(app)

socketio= SocketIO(app)

@app.route('/')
def index():
#una vista web para probar los websockets
    return render_template('index.html')

@socketio.on('datos_gps')
def manejo_datos(datos):
##vamos a procesar los datos reciobidos y guardalos en la DB

    gps_id = datos['gps_id']
    latitude= datos['latitude']
    longitude = datos['longitude']

cursor = mysql.connection.cursor()
cursor.execute("INSERT INTO datos_gps (gps_id, latitude, longitude) VALUES (%s, %s, %s)", (gps_id, latitude, longitude))
mysql.connection.commit()
cursor.close()

@app.route('/gps/<int:gps_id>', methods=['GET'])
def obtenerDatos(gps_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM datos_gps WHERE gps_id = %s", (gps_id,))
    datos = cursor.fetchall()
    cursor.close()

    if not datos:
        return jsonify({'mensaje': 'No se encontro el gps'}), 404
    
    fmt = request.args.get('format','json')


    if fmt == 'json':
        return jsonify(datos)
    elif fmt == 'xml':
        import xml.etree.ElementTree as ET
        raiz = ET.Element('datos_gps')

        for registro in datos:
            elemento = ET.SubElement(raiz, 'georef')
            ET.SubElement(elemento, 'id').text = str(registro[0])
            ET.SubElement(elemento, 'gps_id').text = str(registro[1])
            ET.SubElement(elemento, 'latitude').text = str(registro[2])
            ET.SubElement(elemento, 'longitude').text = str(registro[3])

        datos_xml = ET.tostring(raiz, encoding='utf8')

        return datos_xml, {'Content-Type': 'application/xml'}
    
    else:
        return jsonify({'mensaje': 'Formato no soportado'}), 400
    


#####Desplegar todos los mardaodres en el mapa#####


@app.route('/mapa/todos', methods=['GET'])
def verTodoMapa():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT latitude, longitude FROM datos_gps")
    datos= cursor.fetchall()
    cursor.close()

    return jsonify('todos.html', datos=datos)  

if __name__ == '__main__':
    socketio.run(app, debug=True)
