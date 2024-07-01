import imghdr
import smtplib
from email.message import EmailMessage

SENDER = 'markfu1996@gmail.com'
RECEIVER = 'markfu1996@gmail.com'
PASSWORD = 'xxx'

def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'New Customer show up!'
    email_message.set_content('Hey, we just saw a new customer')

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image',
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER,RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == '__main__':
    send_email(image_path='images/9.png')