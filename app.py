from flask import Flask
from flask_restplus import Api
from api import observations

flask_app = Flask(__name__)
flask_api = Api(flask_app)

flask_api.add_namespace(observations.api, path='/observations')
# BOM site map - http://www.bom.gov.au/site-map/


if __name__ == '__main__':
    flask_app.run(debug=True)