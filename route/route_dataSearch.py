from flask import Blueprint, request, jsonify, render_template
from models.model_dataSearch import model_dataSearch

main = Blueprint('dataSearch_bp', __name__)


@main.route('/getdata', methods=['POST'])
def data_search():
    co_ubigeo = request.form['codubigeo']
    departamento = model_dataSearch.get_data(co_ubigeo)

    return jsonify({'departamento': departamento})

@main.route('/')
def index():
    return  render_template('index.html')