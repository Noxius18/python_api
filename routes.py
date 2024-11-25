from flask_restful import Api
from flask import Blueprint
from models import Buku, CariBuku, UpdateBuku

buku_bp = Blueprint('buku', __name__)
api = Api(buku_bp)

# Route untuk melihat daftar Buku (GET) dan Menambah Buku Baru (POST)
api.add_resource(Buku, '/api/buku/')

# Route untuk mencari buku berdasarkan id
api.add_resource(CariBuku, '/api/buku/<int:id>')

# Route untuk update buku (PATCH) dan menghapus buku (DELETE) berdasarkan id
api.add_resource(UpdateBuku, '/api/buku/<int:id>')