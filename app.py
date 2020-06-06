from flask import Flask, render_template, request, jsonify
from flask_api import status
import configparser
import psycopg2



app = Flask(__name__)
config = configparser.ConfigParser()
config.read('padronapi.ini')
cnx=psycopg2.connect(dbname=config['DB']['name'], user=config['DB']['user'], password=config['DB']['password'], host=config['DB']['host'], port=config['DB']['port'])
cur=cnx.cursor()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api/v1/provincias',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincias():
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia;")
        dataJson = []
        for provincia in cur.fetchall():
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/provincias',methods=['POST', 'GET', 'DELETE', 'PUT'])
def mostrar_provincias():
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia;")
        dataJson = []
        for provincia in cur.fetchall():
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED










@app.route('/api/v1/provincia/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia WHERE codigo=%s;",(codigo,))
        provincia=cur.fetchone()
        if provincia is None :
            content = {'Error de código': 'La provincia con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v1/cantones',methods=['POST', 'GET', 'DELETE', 'PUT'])
def cantones():
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton;")
        dataJson = []
        for cantones in cur.fetchall():
            dataDict = {
                'codigo': cantones[1],
                'nombre': cantones[2]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para cantones'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v1/canton/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def canton(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton WHERE codigo=%s;",(codigo,))
        canton=cur.fetchone()
        if canton is None :
            content = {'Error de código': 'El Cantón con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': canton[1],
                'nombre': canton[2]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para canton'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED


@app.route('/api/v1/distrito/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def distrito(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE codigo=%s;",(codigo,))
        distrito=cur.fetchone()
        if distrito is None :
            content = {'Error de código': 'El distrito con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': distrito[2],
                'nombre': distrito[3]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para distrito'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v1/distritos',methods=['POST', 'GET', 'DELETE', 'PUT'])
def distritos():
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito;")
        dataJson = []
        for distritos in cur.fetchall():
            dataDict = {
                'codigo': distritos[2],
                'nombre': distritos[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para distritos'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED


        
if __name__ == '__main__':
    app.debug = True
    app.run()
