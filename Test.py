import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL')
EMAIL_PASSWORD = os.environ.get('PASS')

def send_mail (link):
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Price fell down!'
    body = f'Check the following link: {link}'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'hristiyan.mechkov@yahoo.com',
        'hmechkov1@gmail.com',
        msg
    )
    print('HEY EMAIl HAS BEEN SENT')

    server.quit()
