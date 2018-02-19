from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def route_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = "Logan"
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8000
    )