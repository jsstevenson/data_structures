class EmptyContainerError(Exception):
    def __init__(self, message):
        self.message = message


class NoSuchKeyError(Exception):
    def __init__(self, message):
        self.message = message
