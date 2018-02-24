from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
