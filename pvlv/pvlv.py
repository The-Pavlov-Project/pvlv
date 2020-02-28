from abc import ABC, abstractmethod


class BotInterface(ABC, object):
    def __init__(self):

        self.user_id = None
        self.username = None

        self.guild_id = None
        self.guild_name = None

        self.timestamp = None

    @abstractmethod
    def send_text(self, location, text, parse_mode=False):
        pass

    @abstractmethod
    def reply_text(self, text, parse_mode=False):
        pass

    @abstractmethod
    def send_photo(self, location, picture):
        pass

    @abstractmethod
    def reply_photo(self, picture):
        pass

    @abstractmethod
    def send_file(self, file):
        pass
