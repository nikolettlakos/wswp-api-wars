from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = "Logan"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = "Logan"
    app.run(
        debug=True,
        port=5000
    )
