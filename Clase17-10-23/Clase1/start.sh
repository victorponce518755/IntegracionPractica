#!/usr/bin/bash

export FLASK_APP=server.py
flask run --host=0.0.0.0

##Le damos permisos de ejecucion
chmod 755 start.sh

#### hace el export automatico

./start.sh


####    Copiamos el mapa.html a todos.html
cp mapa.html todos.html