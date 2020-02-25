from flask import Flask
from flask_restplus import Resource, Api, fields
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)

# BOM site map - http://www.bom.gov.au/site-map/

all_obs = api.model('AllObservations', {'foo': fields.String})
city_obs = api.model('CityObservations', {'foo': fields.String})


@api.route('/observations')
class AllObservations(Resource):

    @api.response('200', 'Success', all_obs)
    def get(self):
        '''
        Return summary of all available observations.
        '''
        return { 'foo': 'bar' }


@api.route('/observations/<string:city_name>')
class CityObservations(Resource):
    
    @api.response('200', 'Success', city_obs)
    @api.response('404', 'City not found.')
    def get(self, city_name):
        '''
        Return observations for a specific city.
        '''
        return { 'foo': 'bar' }


if __name__ == '__main__':
    app.run(debug=True)