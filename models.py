from flask_restplus import fields
from app import api

all_obs = api.model('AllObservations', {'foo': fields.String})


city_obs = api.model('CityObservations', {'foo': fields.String})