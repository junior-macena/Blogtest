from flask import Flask, render_template
from datetime import datetime

app = Flask ("hello")

posts = [
    {
        "title": "O meu primeiro post",
        "body": "Aqui e o Texto do Post",
        "author": "Junior",
        "created": datetime(2022,7,25)

    },
    {
        "title": "O meu Segundo post",
        "body": "Aqui e o Texto do Post",
        "author": "Cesar",
        "created": datetime(2022,7,25)
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

