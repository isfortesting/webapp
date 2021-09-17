from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = "something strange"

@app.route('/<data>')
def test(data: str):

    information = ["words", "test"]

    return render_template('index.html', data=information)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def proc():

    email = request.form['email']
    name = request.form['name']

    if name and email:
        newName = name[::-1]

        return jsonify({'name' : newName})

    return jsonify({'error' : 'Missing data!'})
