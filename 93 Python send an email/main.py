import smtplib

sender = "blexbottt2915@gmail.com"
receiver = "blexbottt2915@gmail.com"
password = "gbnneacyrbfmdybk"
subject = "python project 93 test email"
body = """ikaw bobo putanginamo ka bodi putang ina mooobobo
        ka bobo ka tanginamo"""

# header
message = f"""From: Sellen {sender}
To: Blexnginamo {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")

    server.sendmail(sender, receiver, message)
    print("Email has been sent")

except smtplib.SMTPNotSupportedError:
    print("unable to sign in")