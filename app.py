import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from flask import Flask, request, render_template, session


app = Flask(__name__)
app.secret_key = "your_secret_key_here"

sender_email = "sonikasoni.luv@gmail.com"
sender_password = "ogxuxifxumtbenqm"

smtp_server = "smtp.gmail.com"
smtp_port = 587


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_new():
    # if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if username == "sonika" and password == "pass":
        session["username"] = username
        print("Login successful!", "success")
        return render_template("index.html")
    else:
        print(f"Invalid username or password")
    return render_template("wrong.html")
    # return print(f"Invalid username or password")


@app.route("/index")  # type: ignore
def index():
    if "username" in session:
        return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    if "username" not in session:
        print("You need to log in first.", "danger")
        return render_template("login.html")
    else:
        receiver_email = request.form.get("email")
        Name = request.form.get("name")
        meals = request.form.get("meals")
        Canteen = request.form.get("Canteen")
        Tea = request.form.get("Tea")
        Snacks = request.form.get("Snacks")
        slip  = request.form.get("Slip")

        send_mail(receiver_email, Name, meals, Canteen, Tea, Snacks,slip)
        return render_template("index.html")


def send_mail(receiver_email, Name, meals, Canteen, Tea, Snacks, slip ):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = f"{slip} SILP NO FOR MEALS TOKEN"

    body = f"""Dear {Name},

I hope this email finds you well.

We are pleased to inform you that we can deliver {Tea} tea,{ Snacks} snacks , {meals} meals to you at this {Canteen} Canteen.
We are committed to continuing our efforts to support you and we appreciate your ongoing support and collaboration. If you have any questions or need further details, please do not hesitate to reach out.

Thank you for your attention and cooperation. Visit us again"""

    msg.attach(MIMEText(body, "plain"))
    try:
        # Connect to the server and login
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        # Close the connection
        server.quit()  # type: ignore


if __name__ == "__main__":
    app.run(debug=True)
