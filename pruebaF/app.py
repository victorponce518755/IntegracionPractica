from flask import Flask, Response, send_from_directory
import requests
from lxml import etree
import os

app = Flask(__name__)

 

#servir archivos estaticos
app.config['XSLT_FOLDER'] = 'xsl'

@app.route('/xsl/<path:filename>')
def serve_xsl(filename):
    return send_from_directory(app.config['XSLT_FOLDER'], filename)




def transform_xml_to_html(xml_content, xsl_content):
    xml_doc = etree.fromstring(xml_content)
    xslt_doc = etree.fromstring(xsl_content)
    transform = etree.XSLT(xslt_doc)
    result_tree = transform(xml_doc)
    html_content = str(result_tree)
    return html_content

@app.route('/receta/<int:id>')
def display_xml_receta(id):
    # Obtener XML del backend
    backend_url = 'http://35.224.154.129:5000/receta/{}'.format(id)
    response = requests.get(backend_url)

    if response.status_code == 200:
        xml_content = response.text

        # Leer el contenido del archivo XSL
        with open('xsl/TR.xsl', 'r') as xsl_file:
            xsl_content = xsl_file.read()

        # Transformar XML a HTML
        html_content = transform_xml_to_html(xml_content, xsl_content)

        return Response(html_content, content_type='text/html')
    else:
        return "Error al obtener la receta"

if __name__ == '__main__':
    app.run(debug=True, port=5001)