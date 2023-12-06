# Taken from CS50 Finance Project

import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid

from flask import redirect, render_template, session
from functools import wraps


# Function to render an apology message to the user
def apology(message, code=400):
    """Render message as an apology to user."""

    # Function to escape special characters
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s

    # Render apology template with the provided code and escaped message
    return render_template("apology.html", top=code, bottom=escape(message)), code


# Decorator to require login for certain routes
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is logged in
        if session.get("user_id") is None:
            # Redirect to the login page if not logged in
            return redirect("/login")
        # Continue to the original route if logged in
        return f(*args, **kwargs)
    return decorated_function
