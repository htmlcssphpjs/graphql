from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from jinja2 import Environment, FileSystemLoader
import os

def emailt(data, message, to):
    env = Environment(
        loader=FileSystemLoader('%s/html/' % os.path.dirname(__file__)))
    if message == 'delete':
        template = env.get_template('delete.html')
        output = template.render(data=data)
    else:
        template = env.get_template('new.html')
        output = template.render(data=data)
    send(output, to)

def send(message, to):
    msg = MIMEMultipart()

    password = "crewstreet"
    msg['From'] = "cr3wstreet@gmail.com"
    msg['To'] = to
    msg['Subject'] = "CrewStreet"

    msg.attach(MIMEText(message, 'html'))

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()
