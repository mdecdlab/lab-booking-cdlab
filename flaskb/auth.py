import functools
# for authomatic
from authomatic import Authomatic
# from config.py 導入 CONFIG 與 CALLBACK_URL
from config import CONFIG
from config import CALLBACK_URL
from authomatic.adapters import WerkzeugAdapter

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
    , make_response
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskb.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T', report_errors=False)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

'''
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
'''

@bp.route('/autho_index')
def autho_index():

    return render_template('auth/autho_index.html')


@bp.route('/autho_login/<provider_name>/', methods=['GET', 'POST'])
def autho_login(provider_name):

    # We need response object for the WerkzeugAdapter.
    response = make_response()

    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
            # 利用 session 登記登入者的 email (試著將 @ 換為 _at_)
            session['login_email'] = result.user.email.replace('@', '_at_')
            #session['logged_in'] = True
            login_email = session.get('login_email')
            flash('已經登入!')
        # The rest happens inside the template.
        return render_template('auth/autho_login.html', result=result, login_email=login_email, CALLBACK_URL=CALLBACK_URL)

    # Don't forget to return the response.
    return response


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()



@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view