from flask import Flask, render_template, request, jsonify, url_for, json
import os
app = Flask(__name__)

# Pour trouver le fichier JSON
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "book.json")
data = json.load(open(json_url))


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/ma route", methods=['POST', 'GET'])
def route():
    if request.method == 'POST':
        name = request.form
        return render_template('route.html', result=name)


@app.route("/books", methods=['POST', 'GET'])
def books():
    # result = request.json['book']
    # return jsonify({"book": result})
    return data


@app.route("/books id", methods=['POST', 'GET'])
def booksid():
    if request.method == 'POST':
        idbook = request.form
        return render_template('book.html', data=data, idbook=idbook)


if __name__ == '__main__':
    app.run(debug=True)
