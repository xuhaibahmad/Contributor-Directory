from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('home.html', title="Home")


if __name__ == '__main__':
    app.run(debug=True)
