from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
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

# Argument Parser untuk Valisasi Input (POST)
buku_args = reqparse.RequestParser()
buku_args.add_argument('judul', type=str, required=True, help="Judul harus diisi")
buku_args.add_argument('deskripsi', type=str, required=True, help="Deskripsi harus diisi")
buku_args.add_argument('penulis', type=str, required=True, help="Penulis harus diisi")
buku_args.add_argument('genre', type=str, required=True, help="Genre harus diisi")
buku_args.add_argument('tahun', type=int, required=True, help="Tahun harus diisi")

# Format Response (GET JSON)
buku_fields = {
    'id': fields.Integer,
    'judul': fields.String,
    'deskripsi': fields.String,
    'penulis': fields.String,
    'genre': fields.String,
    'tahun': fields.Integer
}

class Buku(Resource):
    # GET Response data buku (dalam bentuk JSON)
    @marshal_with(buku_fields)
    def get(self):
        buku = BukuModel.query.all()
        return buku
    
    # POST Data kedalam Database
    @marshal_with(buku_fields)
    def post(self):
        args = buku_args.parse_args()
        buku_baru = BukuModel(
            judul=args["judul"],
            deskripsi=args["deskripsi"],
            penulis=args["penulis"],
            genre=args["genre"],
            tahun=args["tahun"])
        try: 
            db.session.add(buku_baru)
            db.session.commit()
            return buku_baru, 201
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, message=f"Kesalahan pada Database {err}")

class CariBuku(Resource):
    @marshal_with(buku_fields)
    def get(self, id):
        buku = BukuModel.query.filter_by(id=id).first()
        if not buku:
            abort(404, 'Buku Tidak Ditemukan')
        return buku


def conn_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()