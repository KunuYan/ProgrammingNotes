from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', title='home', data=[{
        'description': 'Todo 1'
    }, {'description': 'Todo 2'
    }, {'description': 'Todo 3'
    }])


if __name__ == "__main__":
    app.run(debug=True)