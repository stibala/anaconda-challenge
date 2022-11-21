
from pydantic import BaseModel


class BaseAPIModel(BaseModel):
    """Base model"""

    def __eq__(self, other: object):
        return all([value == getattr(other, key) for key, value in self])
