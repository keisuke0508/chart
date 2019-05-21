import os

from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET'])
def get():
    return render_template(
        'index.html',
    )


@app.route('/', methods=['POST'])
def post():
    return render_template(
        'index.html',
    )


if __name__ == '__main__':
    app.run();
