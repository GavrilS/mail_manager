from clean_up import MailCleaner


MAIL_CLEANER_ALLOWED_COMMANDS = [
    'clean_mails',
    'clean_and_save_mails',
    'read_mails'
]

PROCESSES = ['mail_cleaner']


def run_process(*args, **kwargs):
    if 'mail_cleaner' in kwargs.get('process', ''):
        cleaner = MailCleaner(
            kwargs.get('connector', None),
            kwargs.get('db', None),
            kwargs.get('to_clean', False),
            kwargs.get('read_only', False),
            kwargs.get('to_save', False)
        )

        cleaner()
