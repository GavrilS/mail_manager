import os
import imaplib
import email
from email.header import decode_header
import webbrowser


class ImapConnector:

    def __init__(self, username, password, imap_server):
        self.username = username
        self.password = password
        self.imap_server = imap_server
 
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not username:
            raise Exception('Missing username - cannot setup MailConnector class!')
        self._username = username
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        if not password:
            raise Exception('Missing password - cannot setup MailConenctor class!')
        self._password = password

    @property
    def imap_server(self):
        return self._imap_server
    
    @imap_server.setter
    def imap_server(self, imap_server):
        if not imap_server:
            raise Exception('Missing imap server - cannot setup MailConnector class!')
        self._imap_server = imap_server

    def connect_to_mail_box(self):
        imap = imaplib.IMAP4_SSL(self.imap_server)
        imap.login(self.username, self.password)
        self.imap = imap

    def logout(self):
        self.imap.logout()
