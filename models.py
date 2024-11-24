from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Buku(db.Model):
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

def conn_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()

