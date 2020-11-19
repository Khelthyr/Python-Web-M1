from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/ma route", methods=['POST', 'GET'])
def route():
    if request.method == 'POST':
        name = request.form
        return render_template('route.html', result=name)


if __name__ == '__main__':
    app.run(debug=True)
