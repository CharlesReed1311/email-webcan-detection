import os 
import smtplib
from email.message import EmailMessage
import mimetypes

PASSWORD = os.getenv("PASSWORD")
SENDER = "chaitanyaarora345@gmail.com"
RECEIVER = "chaitanyaarora345@gmail.com"
def send_email(imagepath):
    message = EmailMessage()
    message["Subject"] = "new customer showed up"
    message.set_content("Hey, we just saw a new customer")

    with open(imagepath, "rb") as file:
        content = file.read()

    ctype, _ = mimetypes.guess_type(imagepath)
    maintype, subtype = ctype.split(r'/')

    message.add_attachment(content, maintype=maintype, subtype=subtype)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, message.as_string())
    gmail.quit()

