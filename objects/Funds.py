import json

from objects.FileStorage import FileStorage


class Funds(FileStorage):
    file_name = 'funds.json'

    def __init__(self):
        super().__init__()
        self.copper = self._get('copper')
        self.silver = self._get('silver')
        self.gold = self._get('gold')
        self.platinum = self._get('platinum')

    def to_dict(self) -> dict:
        return {
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
        print(f'Saving: {self.to_dict()}...')
        with open(self.file_name, 'w') as f:
            json.dump(self.to_dict(), f)
