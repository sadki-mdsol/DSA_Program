from flask import Flask,jsonify

app = Flask(__name__)

# @app.route('/<name>')
# def index_name(name):
#     return '<h1>Hello {}!</h1>'.format(name)


@app.route('/')
def index():
    return '<h1>Hello World !</h1>'

@app.route('/home')
def home():
    return '<h1>You are at home page!.....</h1>'

@app.route('/json')
def json():
    return jsonify({'key':'val1','list_key':[1,2,3,]})


if __name__ == '__main__':
    app.run(debug=True)