import os
from connectors.imap_connector import ImapConnector
from connectors.pop_connector import PopConnector
from mail_box_handlers.imap_handler import ImapHandler

MAIL_USERNAME = os.getenv('MAIL_USER', None)
MAIL_PASSWORD = os.getenv('MAIL_PASS', None)
MAIL_SERVER = os.getenv('IMAP_SERVER', None)
MAIL_PORT = os.getenv('POP_PORT', None)
CONNECTOR = os.getenv('CONNECTOR', 'imap')

DEFAULT_MAIL_FOLDER = ''

# def main(handler, connector):
#     handler.get_messages(DEFAULT_MAIL_FOLDER)
#     connector.logout()


def imap_setup(creds):
    connector = ImapConnector(
        creds.get('username', None), 
        creds.get('password', None), 
        creds.get('imap_server', None)
    )

    connector.connect_to_mail_box()
    handler = ImapHandler(connector.imap)

    return handler, connector

def pop_setup(creds):
    connector = PopConnector(
        creds.get('username', None), 
        creds.get('password', None), 
        creds.get('imap_server', None)
    )

if __name__=='__main__':
    creds = {
        'username': MAIL_USERNAME,
        'password': MAIL_PASSWORD,
        'server': MAIL_SERVER,
        'port': MAIL_PORT
    }

    handler, connector = setup(creds)
    main(handler, connector)
