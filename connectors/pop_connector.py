import poplib

class PopConnector:

    def __init__(self, username, password, server, port):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
    
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
    def server(self):
        return self._server
    
    @server.setter
    def server(self, server):
        if not server:
            raise Exception('Missing server - cannot setup MailConnector class!')
        self._server = server

    @property
    def port(self):
        return self.port
    
    @port.setter
    def port(self, port):
        if not port:
            raise Exception('Missing port - cannot setup MailConnector class!')
        self._port = port

    def connect(self):
        mailbox = poplib.POP3_SSL(self.server, self.port)
        mailbox.user(self.username)
        mailbox.pass_(self.password)
        self.mailbox = mailbox
    
    def quit(self):
        self.mailbox.quit()

    def get_num_available_messages(self):
        return len(self.mailbox.list()[1]) # TODO Add error handling
    
    def get_messages(self, message_count=10):
        available_messages = self.get_num_available_messages()
        if available_messages < message_count:
            message_count = available_messages
            print(f"There are only {available_messages} in the mailbox - showing all of them!")
        
        for i in range(available_messages):
            for msg in self.mailbox.retr(i+1)[1]:
                print(msg)
                print('='*100)
        

