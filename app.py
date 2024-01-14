from flask import Flask, session, redirect, url_for, render_template
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key for sessions


@app.route("/")
def home():
    return "Welcome to the Flask OAuth Playground!"


@app.route("/login")
def login():
    # Simulate OAuth login
    session["user_id"] = 1
    return redirect(url_for("profile"))


@app.route("/profile")
def profile():
    # Access user_id from the session (simulating OAuth session)
    user_id = session.get("user_id")

    if user_id:
        # Simulate fetching user data using OAuth
        user_data = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        ).json()
        return render_template("profile.html", user_data=user_data)
    else:
        return "Login first to view the profile."


if __name__ == "__main__":
    app.run(debug=True)
