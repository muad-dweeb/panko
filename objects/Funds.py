import json
import os
from typing import Union

from discord import Guild, TextChannel

from objects.FileStorage import FileStorage


class Funds(FileStorage):

    def __init__(self, source: Union[Guild, TextChannel]):
        self.__source = source
        self.__prep()

        super().__init__()

        self.copper = self._get('copper')
        self.silver = self._get('silver')
        self.gold = self._get('gold')
        self.platinum = self._get('platinum')

    @staticmethod
    def __prep():
        if not os.path.isdir('./data'):
            os.mkdir('./data')

    @property
    def file_name(self):
        return f'data/{self.__source.id}.json'

    def to_dict(self) -> dict:
        return {
            '_source': str(self.__source),
            'copper': self.copper,
            'silver': self.silver,
            'gold': self.gold,
            'platinum': self.platinum
        }

    def _get(self, key: str) -> int:
        if key in self._loaded.keys():
            return self._loaded[key]
        else:
            self._loaded[key] = 0
            return 0

    def save(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.to_dict(), f)
