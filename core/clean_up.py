class CleanUp:

    def __init__(self, to_clean=False, read_only=False, to_save=False):
        self.set_flags(to_clean, read_only, to_save)

    def run(self):
        if self.to_clean:
            if self.to_save:
                self.clean_and_save_mails()
            else:
                self.clean_mails()
        elif self.read_only:
            self.read_mails()

    __call__ = run

    def set_flags(self, to_clean=False, read_only=False, to_save=False):
        self.to_clean = to_clean
        self.read_only = read_only
        self.to_save = to_save

    def clean_mails(self):
        pass

    def clean_and_save_mails(self):
        pass
    
    def read_mails(self):
        pass
