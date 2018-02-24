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


@app.route("/registration", methods=['GET', 'POST'])
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


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        data = data_manager.login(username)
        if not data:
            return redirect(url_for('index', log=False))
        user_id = data_manager.get_id_by_username(username)['user_id']
        session['username'] = username
        session['user_id'] = user_id
        log = data_manager.verify_password(request.form.to_dict()['password'], data[0]['password'])
        if log:
            return redirect(url_for('index'))
        else:
            session.pop('username', None)
            session.pop('user_id', None)
            log = False
            return redirect(url_for('index', log=False))
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8000
    )