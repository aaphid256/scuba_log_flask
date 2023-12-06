import os

from cs50 import SQL
import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Username is Empty")
        if not password:
            return apology("Password is Empty")
        if not confirmation:
            return apology("Confirmation is Empty")
        if password != confirmation:
            return apology("Password and Confirmation Must Match")

        pass_hash = generate_password_hash(password)

        try:
            new_user = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, pass_hash
            )
        except:
            return apology("Username Already Exists")

        session["user_id"] = new_user

        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/")
@login_required
def index():
    """Show dive log summary for the logged-in user"""

    # Retrieve user_id from the session
    user_id = session["user_id"]

    # Query the database to retrieve dive log data for the user, ordered by date in descending order
    dives = db.execute(
        "SELECT dive_num, date, location, surf_int, time_in, dive_time, max_depth, avg_depth, gas_used, notes FROM dive_log WHERE user_id = ? ORDER BY date DESC",
        user_id,
    )

    # Query the database to retrieve the username of the logged-in user
    user_name_db = db.execute(
        "SELECT username FROM users WHERE id = ?", user_id)
    name = user_name_db[0]["username"]

    # Calculate the total dive time for all dives
    total_time = datetime.timedelta()
    for dive in dives:
        (h, m, s) = dive["dive_time"].split(":")
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total_time += d

    # Render the HTML template with dive log data and total dive time
    return render_template(
        "index.html",
        dives=dives,
        total_time=total_time
    )


@app.route("/dive_log", methods=["GET", "POST"])
@login_required
def dive_log():
    """Log dive"""

    # If the request method is GET, display the dive log form
    if request.method == "GET":
        return render_template("dive_log.html")

    # If the request method is POST, handle form submission to log a new dive
    else:
        #
        # Form data
        dive_num = request.form.get("dive_num")
        date = request.form.get("date")
        location = request.form.get("location")
        surf_int = request.form.get("surf_int")
        time_in = request.form.get("time_in")
        dive_time = request.form.get("dive_time")
        max_depth = request.form.get("max_depth")
        avg_depth = request.form.get("avg_depth")
        gas_used = request.form.get("gas_used")
        notes = request.form.get("notes")

        # Validate form data
        if not dive_num:
            return apology("Enter dive number")
        if not date:
            return apology("Enter date")
        if not dive_time:
            return apology("Enter dive time")
        if not max_depth:
            return apology("Enter max depth")

        # Retrieve user_id from the session
        user_id = session["user_id"]

        # Insert the new dive log entry into the database
        db.execute(
            "INSERT INTO dive_log (user_id, dive_num, date, location, surf_int, time_in, dive_time, max_depth, avg_depth, gas_used, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            user_id,
            dive_num,
            date,
            location,
            surf_int,
            time_in,
            dive_time,
            max_depth,
            avg_depth,
            gas_used,
            notes
        )

        # Flash a success message
        flash(
            f"Success! Log {dive_num} entered!"
        )

        # Redirect to the index page after logging the dive
        return redirect("/")


@app.route("/gear_log", methods=["GET", "POST"])
@login_required
def gear_log():
    """View and log gear information"""

    # If the request method is GET, display the user's gear log
    if request.method == "GET":
        # Retrieve user_id from the session
        user_id = session["user_id"]

        # Query the database to retrieve gear log data for the user
        gear = db.execute(
            "SELECT type, brand, date_purchased, condition, last_service, notes FROM gear_log WHERE user_id = ?",
            user_id,
        )

        # Render the HTML template with the gear log data
        return render_template(
            "gear_log.html",
            gear=gear,
        )

    # If the request method is POST, handle form submission to log new gear
    else:
        # Form data
        type = request.form.get("type")
        brand = request.form.get("brand")
        date_purchased = request.form.get("date_purchased")
        condition = request.form.get("condition")
        last_service = request.form.get("last_service")
        notes = request.form.get("notes")

        # Validate form data
        if not type:
            return apology("Enter type of gear")
        if not date_purchased:
            return apology("Enter the date you received")

        # Retrieve user_id from the session
        user_id = session["user_id"]

        # Insert the new gear log entry into the database
        db.execute(
            "INSERT INTO gear_log (user_id, type, brand, date_purchased, condition, last_service, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
            user_id,
            type,
            brand,
            date_purchased,
            condition,
            last_service,
            notes
        )

        # Flash a success message
        flash(
            f"Success! {type} entered!"
        )

        # Redirect to the gear log page after logging the new gear
        return redirect("/gear_log")


@app.route("/travel", methods=["GET", "POST"])
@login_required
def travel():
    """View and log travel destinations"""

    # If the request method is GET, display the user's travel history
    if request.method == "GET":
        # Retrieve user_id from the session
        user_id = session["user_id"]

        # Query the database to retrieve travel history for the user
        locations = db.execute(
            "SELECT destination, date, notes FROM travel WHERE user_id = ?",
            user_id,
        )

        # Render the HTML template with the travel history data
        return render_template(
            "travel.html",
            locations=locations,
        )

    # If the request method is POST, handle form submission to log a new travel destination
    else:
        # Form data
        destination = request.form.get("destination")
        date = request.form.get("date")
        notes = request.form.get("notes")

        # Validate form data
        if not destination:
            return apology("Enter destination name")
        if not date:
            return apology("Enter a travel date")

        # Retrieve user_id from the session
        user_id = session["user_id"]

        # Insert the new travel destination entry into the database
        db.execute(
            "INSERT INTO travel (user_id, destination, date, notes) VALUES (?, ?, ?, ?)",
            user_id,
            destination,
            date,
            notes
        )

        # Flash a success message
        flash(
            f"Success! {destination} entered!"
        )

        # Redirect to the travel page after logging the new destination
        return redirect("/travel")
