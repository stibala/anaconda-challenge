"""Exceptions module"""


class DbItemNotFoundError(Exception):
    def __init__(self, model, item_id):
        self.model = model
        self.id = item_id

    def __str__(self):
        return f"Not Found: {self.model.__name__}(id={self.id})"


class TurnFinishedError(Exception):
    def __init__(self, item_id):
        self.id = item_id

    def __str__(self):
        return f"Turn finished (id={self.id})"


class InvalidThrowUsernameError(Exception):
    def __init__(self, allowed):
        self.allowed = allowed

    def __str__(self):
        return f"Bad username: allowed are {self.allowed}"
