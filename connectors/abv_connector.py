from pop_connector import PopConnector

SEARCHED_MESSAGE_ATTRIBUTES = 4

class PopAbvConnector(PopConnector):

    def __init__(self, username, password, server, port):
        super().__init__(username, password, server, port)

    def get_messages(self, message_count=10):
        message_count = self._verify_num_available_messages(message_count)
        messages = []
        for i in range(message_count):
            message_attributes = {}
            attributes_found = 0
            for msg in self.mailbox.retr(i+1)[1]:
                if b'Date: ' in msg:
                    message_attributes['date'] = msg.decode('utf-8')
                    attributes_found += 1
                elif b'To: ' in msg:
                    message_attributes['receivers'] = msg.decode('utf-8')
                    attributes_found += 1
                elif b"Subject: " in msg:
                    message_attributes['subject'] = msg.decode('utf-8')
                    attributes_found += 1
                elif b'From: ' in msg:
                    message_attributes['sender'] = msg.decode('utf-8')
                    attributes_found += 1
                
                if attributes_found == SEARCHED_MESSAGE_ATTRIBUTES:
                    break
            
            messages.append(message_attributes)
        
        return messages
