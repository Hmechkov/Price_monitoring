import smtplib

def send_mail (link):
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hristiyan.mechkov@yahoo.com', '30$JustinianYahoo1')

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
