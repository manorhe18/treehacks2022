import getpass
import wikipedia
import csv
import pandas as pd
from tabulate import tabulate



#radr = input("Adresses to log in to")  # address to check and send from
#imapserver = input("IMAP server domain: ")  # imap server for account
#smtpserver = input("SMTP server domain: ")  # smtp server for account
#smtpserverport = 465  # smtp server port for starttls

#pwd =  getpass.getpass("Account password: ") # password for account encoded with base64.b64encode
#sadr = input("Trusted addresses to receive from: ")  # address to receive commands from
radr = 'opencell2022@gmail.com'
imapserver = 'imap.gmail.com'
smtpserver = 'imap.gmail.com'
smtpserverport = 465
pwd = 'treehacks2022'
sadr = 'rheanano16@gmail.com'
check_freq = 5

def help_fn(lines):
    text = """Hello! Welcome to our SearchBot. Below is a list of available commands you can run:
            wikipedia = use this to search for anything on Wikipedia eg. 'wikipedia Michael Jordan'
            ask = use this platform to ask questions about health-care, financial support, and other life-planning
                        e.g. 'ask how do I find a job once I am out of prison?'
            resources = this will return a table of organizations whom you can reach out to
                        just type 'resources' 
            please note: You can only send one command at a time. It must be the first word on the first line of your email message.
                         All emails are strictly monitored by the facility under which you are housed.
                Thank you!
            """
    return text

def resourcetable(lines):
    a = pd.read_csv('resources.csv')
    text = ''
    for i in range(1, 10):
        arr = a.iloc[i].to_numpy()
        for e in arr:
            text = text + str(e) + '\n'
        text = text + '\n'
    return text

def out_connect(lines):
    return "Your question has been posted! We will email you back once someone has submitted an answer"

def wikicontent(lines):
    q = lines[10:]
    page = wikipedia.page(wikipedia.search(q)[0])
    content = page.content
    return content

commands = {"help" : help_fn, "wikipedia": wikicontent, "resources": resourcetable, "ask": out_connect}