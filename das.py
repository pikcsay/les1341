from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def train(prof):
    params = {
        'prof': prof
    }

    return render_template('prof.html', **params)


if __name__ == '__main__':
    app.run(port=5000, host='localhost')
