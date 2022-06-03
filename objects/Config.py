import os

from discord import Colour

from objects.FileStorage import FileStorage


class Config(FileStorage):
    file_name = 'config.json'
    file_required = True

    def __init__(self):
        super().__init__()
        self.token = self._loaded['token']
        self.add_url = self._loaded['add_url']
        self.color = Colour.gold()
        self.homepage = self._loaded['homepage']
        self.version = self._loaded['version']
        self.license = self._loaded['license']

        git_root = self.homepage.split('#')[0]
        self.icon = os.path.join(git_root,
                                 'blob/main/images/icon.png?raw=true')
