import json
from dataclasses import dataclass
from enum import IntEnum

class ContentType(IntEnum):
    text = 1
    attachment = 2

@dataclass
class Payload:
    content: str = ''
    content_type: ContentType = ContentType.text

    @classmethod
    def from_bytes(cls, data: bytes) -> 'Payload':
        serialized = data.decode()
        self_dict = json.loads(serialized)
        print(self_dict)

        return Payload(**self_dict)

    def __bytes__(self):
        """Вызывается функцией bytes(obj)"""
        self_dict = self.__dict__
        print(self_dict)
        serialized = json.dumps(self_dict)

        return serialized.encode()
