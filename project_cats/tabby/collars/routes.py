from flask import render_template, request, flash, redirect, url_for

from . import collars



@collars.route('/register', methods=['GET', 'POST'])
def register_splash():
    return render_template("users/register.html")


