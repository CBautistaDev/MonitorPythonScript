import requests
import smtplib
import os
#avbmxmyariewxofu

from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
print(EMAIL_ADDRESS, EMAIL_PASSWORD)
r = requests.get('https://status.slack.com/', timeout=5)

# if r.status_code != 200:
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'YOUR SITE IS DOWN!'
    body = 'Make sure the server restarted and it is back up'
    msg = f'Subject: {subject}\n\n{body}'

    # logging.info('Sending Email...')
    smtp.sendmail(EMAIL_ADDRESS, 'cbautista2013@gmail.com', msg)