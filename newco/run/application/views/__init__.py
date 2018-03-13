#!/usr/bin/env python3

from flask import Blueprint, render_template, request


module = Blueprint('views', __name__, url_prefix="")


# Front page
@module.route('/', methods=['GET'])
def front():
    return render_template('index.html')


# 404 page
@module.route('/404', methods=['GET'])
def error_404():
    return render_template('404.html')


# Register page
@module.route('/register', methods=['GET', 'POST'])
def register():
    # Check if the username and password were submitted
        # Check if the username exists
            # Store submitted username and password in the database
    return render_template('register.html')


# Login page
@module.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the username and password were submitted
        # Check if the username exists
            # Check if the submitted password is the stored password for the username
    return render_template('login.html')


###############################################################################
#                                                                             #
# Must be logged in!                                                          #
#                                                                             #
###############################################################################


# Dashboard page
@module.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # TODO Write graphical user interface
    return render_template('dashboard.html')


# Account page
@module.route('/account', methods=['GET', 'POST'])
def account():
    # TODO Write graphical user interface
    return render_template('account.html')


# Note: for local testing
if __name__ == '__main__':
    module.run(debug=True)