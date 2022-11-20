"""Exceptions module"""


class DbItemNotFoundError(Exception):
    def __init__(self, model, item_id):
        self.model = model
        self.id = item_id

    def __str__(self):
        return f"Not Found: {self.model.__name__}(id={self.id})"
