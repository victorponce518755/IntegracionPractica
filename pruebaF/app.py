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


def transform_xml_to_html(xml_content):
    xslt_file= os.path.join('xsl', 'TR.xsl')
    xslt = etree.parse(xslt_file)
    transform = etree.XSLT(xslt)

    xml_doc= etree.fromstring(xml_content)

    html_content = transform(xml_doc)

    html_str = str(html_content)

    return html_str


@app.route('/receta/<int:id>')
def display_xml_receta(id):
    #obtener xml del backend
    backend_url = 'http://35.224.154.129:5000/receta/{}'.format(id)
    response = requests.get(backend_url)
    

    if response.status_code == 200:
        #transformar xml a html
        xml_content = response.text

        print(xml_content)
        html_content = transform_xml_to_html(xml_content)
        
        return Response(html_content, content_type='text/html')
    else:
        return "Error al obtener la receta"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
