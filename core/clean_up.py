class MailCleaner:

    def __init__(self, *args, **kwargs):
        self.set_connector(kwargs.get('connector', None))
        self.set_db(kwargs.get('db', None))
        self.set_flags(
            to_clean=kwargs.get('to_clean', False),
            read_only=kwargs.get('read_only', False),
            to_save=kwargs.get('to_save', False)
        )

    def run(self):
        if self.to_clean:
            if self.to_save:
                self.clean_and_save_mails()
            else:
                self.clean_mails()
        elif self.read_only:
            self.read_mails()
        else:
            print('No option was selected for mail clean up!')

    __call__ = run

    def set_connector(self, connector):
        if not connector:
            raise Exception('Connector instance is missing!')
        self.connector = connector

    def set_db(self, db):
        if not db:
            raise Exception('DB instance is missing!')
        self.db = db

    def set_flags(self, to_clean=False, read_only=False, to_save=False):
        self.to_clean = to_clean
        self.read_only = read_only
        self.to_save = to_save

    def clean_mails(self, message_count):
        self.connector.delete_messages(message_count)

    def clean_and_save_mails(self, message_count):
        messages = self.connector.get_messages(message_count)
        # TODO add messages to DB
        # self.clean_mails(message_count)
    
    def read_mails(self, message_count):
        messages = self.connector.get_messages(message_count)
        if messages:
            print('Messages for connector - ', self.connector)
            print('='*100)
            for msg in messages:
                print(msg)
                print('='*100)
        print('End of retrieved messages!\n', '='*100)
