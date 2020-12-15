import csv
import os
import requests
import smtplib
from dotenv import load_dotenv
from io import StringIO

contacts = {}
body_template = """\
You will be sending a gift to {}.

{}\
"""
email_template = """\
From: {}
To: {}
Subject: {}

{}

🤖 beep boop im a robot. \
pls no reply.
"""

def get_credentials():
    load_dotenv()
    username = os.getenv('GMAIL_USERNAME')
    password = os.getenv('GMAIL_PASSWORD')
    return username, password

def write_mail(name):
    contact = contacts[name]
    sender = 'Raph'
    to = contact['email']
    subject = '🎁 Secret Santa 2020 🎄'
    recipient = contact['to']
    address = contacts[recipient]['address']
    body = body_template.format(recipient, address)
    email = email_template.format(sender, to, subject, body)
    return sender, to, email.encode('utf-8')

def send_mails():
    try:
        print('connecting...')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo_or_helo_if_needed()
        username, password = get_credentials()
        print('logging in as {}...'.format(username))
        server.login(username, password)
        print('login successful!')
        for name in contacts:
            print('sending mail to {}...'.format(name))
            server.sendmail(*write_mail(name))
    except:
        print('failed to send email.')
    finally:
        server.close()
        print('server closed.')

def download_data():
    load_dotenv()
    file_id = os.getenv('CONTACT_INFO_FILE_ID')
    output_format = 'csv'
    url = 'https://docs.google.com/spreadsheet/ccc?key={}&output={}'
    response = requests.get(url.format(file_id, output_format))
    if response.status_code != 200:
        print('failed to download data.')
        return
    return response.content.decode('utf-8')

def map_csv_to_contacts(csvf):
    reader = csv.DictReader(csvf,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        name = row['Name']
        contacts[name] = {}
        contacts[name]['email'] = row['Email']
        contacts[name]['address'] = row['Address']

def cycle(items, cycle=[]):
    bag = set(items)
    while len(bag) > 0:
        cycle.append(bag.pop())
    return cycle

def assign_santas():
    santa_cycle = cycle(contacts.keys())
    for i, santa in enumerate(santa_cycle):
        recipient = santa_cycle[(i + 1) % len(santa_cycle)]
        contacts[santa]['to'] = recipient
        # contacts[recipient]['from'] = santa

csv_data = download_data()
csv_file = StringIO(csv_data)
map_csv_to_contacts(csv_file)
assign_santas()
for name, info in contacts.items():
    print(name, info)

# Uncomment next line to send e-mails
# send_mails()
