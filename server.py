from flask import Flask, render_template, redirect, session, request, escape, url_for
app = Flask(__name__)
app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"


@app.route("/")
def index():
    if 'username' in session:
        user_name = session['username']
        return render_template("index.html", user_name=user_name)
    else:
        return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run(
        debug=True,
        port=5000
    )
