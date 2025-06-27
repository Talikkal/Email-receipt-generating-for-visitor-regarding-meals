import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Email credentials
sender_email = "sonikasoni.luv@gmail.com"
sender_password = "ogxuxifxumtbenqm"
receiver_email = "sonika.talikkal21@gmail.com"


# Set up the server
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For SSL use 465, for TLS use 587

# Create the email headers
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email"

# Create the email body
body = "This is a test email sent from Python!"
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
    server.quit() # type: ignore
