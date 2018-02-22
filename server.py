from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run(
        debug=True,
        port=5000
    )
