import os
from connectors.imap_connector import ImapConnector
from mail_box_handlers.imap_handler import ImapHandler

IMAP_USERNAME = os.getenv('IMAP_USER', None)
IMAP_PASSWORD = os.getenv('IMAP_PASS', None)
IMAP_SERVER = os.getenv('IMAP_SERVER', None)

DEFAULT_MAIL_FOLDER = ''

def main(handler, connector):
    handler.get_messages(DEFAULT_MAIL_FOLDER)
    connector.logout()


def setup(creds):
    connector = ImapConnector(
        creds.get('username', None), 
        creds.get('password', None), 
        creds.get('imap_server', None)
    )

    connector.connect_to_mail_box()
    handler = ImapHandler(connector.imap)

    return handler, connector


if __name__=='__main__':
    creds = {
        'username': IMAP_USERNAME,
        'password': IMAP_PASSWORD,
        'imap_server': IMAP_SERVER
    }

    handler, connector = setup(creds)
    main(handler, connector)
