from flask import render_template, request, flash, redirect, url_for

from . import collars



@collars.route('/register', methods=['GET'])
def register_splash():
    return render_template("users/register.html")


@collars.route('/register/<user:str>', methods=['POST'])
def register_user(user:str):
    pass