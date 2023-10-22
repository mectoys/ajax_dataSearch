from flask import Blueprint, request, jsonify, render_template
from models.model_dataSearch import model_dataSearch

main = Blueprint('dataSearch_bp', __name__)


@main.route('/getdata', methods=['POST'])
def data_search():
    cod_ubigeo = request.form['codubigeo']  # Obtener el valor del input
    print(cod_ubigeo)
    departamento = model_dataSearch.get_data(cod_ubigeo)
    print(departamento)
    #función en Flask que se utiliza para serializar objetos en formato JSON
    #y devolverlos como respuesta en una ruta
    return jsonify({'departamento': departamento})


@main.route('/')
def index():
    return render_template('index.html')
