from flask import Blueprint
from flask import render_template, redirect, flash, request, jsonify
from app.forms import LoginForm

routes_main = Blueprint('routes_main', __name__)


@routes_main.route('/')
def index():
    return render_template('landing/index.html', title='blog')


@routes_main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Logging user {}'.format(form.username.data))
        return redirect('/')

    return render_template('landing/login.html', title='Sign In', form=form)


@routes_main.route('/ident')
def ident_request():
    headers = {k: v for k, v in request.headers}
    headers.update({
        'remote_addr': request.remote_addr
    })
    return jsonify(headers)
