from flask import Flask, render_template, redirect, session, request, escape, url_for
import data_manager
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
    if request.method == 'POST':
        user = data_manager.user_checking(request.form['username'])
        if len(user) == 0:
            password = data_manager.hash_password(request.form['password'])
            login_name = request.form['username']
            data_manager.registration(login_name, password)
            return redirect(url_for('index', already_used=False))
        else:
            return redirect(url_for('registration', already_used=True))
    return render_template('registration.html', already_used=False)


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
