from flask import Flask, render_template, request, url_for
import altair as alt
alt.data_transformers.disable_max_rows()

app = Flask(__name__)

# constants
tableau10 = ["#4e79a7", '#59a14f', '#9c755f', '#f28e2b', "#edc948", '#bab0ac', '#e15759', '#b07aa1', '#76b7b2', '#ff9da7']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/national")
def national():
    return render_template("national.html")

@app.route("/size")
def size():
    return render_template("size.html")

@app.route("/state")
def state():
    return render_template("state.html")

@app.route("/urban")
def urban():
    return render_template("urban.html")

@app.route("/mass")
def mass():
    return render_template("mass.html")

@app.route("/corr", methods=["GET", "POST"])
def corr():

    return render_template("corr.html")

if __name__ == "__main__":
    app.run(debug=True)
