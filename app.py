from flask import Flask
from models import conn_db
from routes import buku_bp

app = Flask(__name__)

# Inisialisasi Database
conn_db(app)

# Mengambil bluprint route dari file route.py
app.register_blueprint(buku_bp)

@app.route("/")
def hello():
    return "<h2>Hello Flask!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
