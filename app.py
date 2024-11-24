from flask import Flask
from models import conn_db

app = Flask(__name__)

# Inisialisasi Database
conn_db(app)

@app.route("/")
def hello():
    return "<h2>Hello Flask!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
