import email
from email.header import decode_header

class ImapHandler:

    def __init__(self, connector):
        self._connector = connector
    
    @property
    def connector(self):
        return self._connector
    
    def get_messages(self, folder, message_count=10):
        status, messages = self.connector.select(folder)

        for i in range(message_count):
            res, msg = self.connector.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg['Subject'])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding)
                    
                    From, encoding = decode_header(msg.get('From'))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)

                    print('Subject: ', subject)
                    print('From: ', From)

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get('Content-Disposition'))
                            try:
                                body = part.get_payload(decode=True).decode()
                            
                            except Exception as e:
                                pass
                            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                                print('Body: ', body)
                            
                            # elif 'attachment' in content_disposition:
                            #     filename = part.get_filename()
                            #     if filename:
                            #         folder_name = clean(subject)

                    else:
                        content_type = msg.get_content_type()
                        body = msg.get_payload(decode=True).decode()
                        if content_type == 'text/plain':
                            print('Body: ', body)
                        elif content_type == 'text/html':
                            print('HTML body: ', body)

                    print('='*100)
