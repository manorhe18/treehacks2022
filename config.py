import getpass

radr = input("Adresses to log in to")  # address to check and send from
imapserver = input("IMAP server domain: ")  # imap server for account
smtpserver = input("SMTP server domain: ")  # smtp server for account
smtpserverport = 465  # smtp server port for starttls

pwd =  getpass.getpass("Account password: ") # password for account encoded with base64.b64encode
sadr = input("Trusted addresses to receive from: ")  # address to receive commands from
check_freq = 5

def hello_world(lines):
    return "Hello, World! "

commands = {"hello" : hello_world}