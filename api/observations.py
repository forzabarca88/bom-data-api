from flask_restplus import Resource, Namespace, fields

api = Namespace('observations', description='Get realtime observation data from BOM')

summary_observation = api.model('summary_observation', {
    'foo': fields.String
})
city_observations = api.model('city_observations', {
    'foo': fields.String
})

@api.route('/')
class AllObservations(Resource):

    @api.marshal_list_with(summary_observation)
    def get(self):
        '''
        Return summary of all available observations.
        '''
        return { 'foo': 'bar' }


@api.route('/<string:city_name>')
class CityObservations(Resource):
    
    @api.marshal_with(city_observations)
    def get(self, city_name):
        '''
        Return observations for a specific city.
        '''
        return { 'foo': 'bar' }
