class UserIsAdmin(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ChannelTypeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
