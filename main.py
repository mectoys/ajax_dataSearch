from flask import Flask
from route import route_dataSearch

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(route_dataSearch.main, url_prefix='/')

    app.run(debug=True)
