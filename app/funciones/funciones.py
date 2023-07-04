
from flask import render_template


def inicio():
    return render_template('base_index.html')


def editProfile():
    return render_template('public/pages/info.html')


def not_found(error):
    return render_template('404.html', error=error)


def server_error(error):
    return render_template('500.html', error=error)
