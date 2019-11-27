import requests
import smtplib
import schedule
import time
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def get_pdf():
    # Standard info for your email configuration
    HOST = "smtp.host.pl"
    MY_ADDRESS = "myemail@gmail.com
    SENDER_ADDRESS = "receiveremail@gmail.com"
    PASSWORD = "password"
    PORT = "PORT NUMBER"
    msg = MIMEMultipart()
    msg['Subject'] = "Your Subject"
    msg['From'] = MY_ADDRESS
    msg['To'] = SENDER_ADDRESS
    today = date.today()
    body = f'''
    Hello Everybody

        Your message 

    Greetings
    '''
    msg.attach((MIMEText(body, 'plain')))

    # your URL to PDF address
    url = "http://localhost:3000/your/pdf/file"
    r = requests.get(url, stream=True)

    with open(f"./YourPDF {str(today)}.pdf", 'wb') as f:
        f.write(r.content)

    # attaching PDF to email message
    pdf_attachment = MIMEApplication(r.content, _subtype="pdf")
    pdf_attachment.add_header(
        'content-disposition',
        'attachment',
        filename=('utf-8', '', f"YourPDF {str(today)}.pdf")
    )
    msg.attach(pdf_attachment)

    # loging and sending message
    server = smtplib.SMTP_SSL(HOST, PORT)
    server.login(MY_ADDRESS, PASSWORD)
    server.sendmail(MY_ADDRESS, SENDER_ADDRESS, msg.as_string())
    server.quit()

# setting schedule for repeating the task, here for 10 minutes
schedule.every(10).minutes.do(get_pdf)

while True:
   schedule.run_pending()
   time.sleep(1)
