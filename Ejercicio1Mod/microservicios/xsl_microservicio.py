from lxml import etree
import os

def transform_xml(xml_string):
    root = etree.fromstring(xml_string)

    arbol_xsl = etree.parse(os.path.join('xsl', 'transformacionR.xsl'))
    transformacion = etree.XSLT(arbol_xsl)
    xml_transformado = transformacion(root)

    return str(xml_transformado)