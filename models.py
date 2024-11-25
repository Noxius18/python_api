from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse, fields, marshal_with, abort

db = SQLAlchemy()

class BukuModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(50), nullable=False)
    deskripsi = db.Column(db.String(255))
    penulis = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(30))
    tahun = db.Column(db.Integer)

    def __repr__(self):
        return f"""Buku(
            Judul = {self.judul},
            Deskripsi = {self.deskripsi},
            Penulis = {self.penulis},
            Genre = {self.genre},
            Tahun = {self.tahun})"""

buku_args = reqparse.RequestParser()
buku_args.add_argument('judul', type=str, required=True, help="Judul harus diisi")
buku_args.add_argument('deskripsi', type=str, required=True, help="Deskripsi harus diisi")
buku_args.add_argument('penulis', type=str, required=True, help="Penulis harus diisi")
buku_args.add_argument('genre', type=str, required=True, help="Genre harus diisi")
buku_args.add_argument('tahun', type=int, required=True, help="Tahun harus diisi")

class Buku(Resource):
    def get(self):
        buku = BukuModel.query.all()
        return buku

def conn_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()

