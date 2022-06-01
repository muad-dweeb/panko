from objects.FileStorage import FileStorage


class Config(FileStorage):
    file_name = 'config.json'
    file_required = True

    def __init__(self):
        super().__init__()
        self.token = self._loaded['token']


