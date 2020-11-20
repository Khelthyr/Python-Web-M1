from flask import Flask, render_template, request, jsonify, url_for, json
import os
app = Flask(__name__)

# Pour trouver le fichier JSON
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "book.json")
jsonData = json.load(open(json_url))


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
    return jsonData


@app.route("/books id", methods=['POST', 'GET'])
def booksid():
    if request.method == 'POST':
        idbook = request.form
        return render_template('bookId.html', data=jsonData, idbook=idbook)
    else:
        return ("Il n'y a pas de livre avec cette id")

        
@app.route("/books titre", methods=['POST', 'GET'])
def bookstitre():
    if request.method == 'POST':
        titre = request.form
        return render_template('bookTitre.html', data=jsonData, titre=titre)
    else:
        return ("Il n'y a pas de livre avec ce titre")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
