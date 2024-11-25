from flask_restful import Api, Resource
from flask import Blueprint
from models import Buku, CariBuku

buku_bp = Blueprint('buku', __name__)
api = Api(buku_bp)

api.add_resource(Buku, '/api/buku/')
api.add_resource(CariBuku, '/api/buku/<int:id>')