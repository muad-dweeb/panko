import json
import os
from abc import abstractmethod
from json import JSONDecodeError


class FileStorage:

    file_required = False

    def __init__(self):
        self._loaded = self.load()

    @property
    @abstractmethod
    def file_name(self):
        raise NotImplementedError

    def load(self) -> dict:
        # Requirement not fulfilled
        if self.file_required and not os.path.isfile(self.file_name):
            raise FileNotFoundError(f'Missing file: {self.file_name}')

        # Initialize
        if not os.path.isfile(self.file_name):
            return dict()

        # Get the goods
        with open(self.file_name, 'r') as f:
            try:
                contents = json.load(f)
                return contents
            except JSONDecodeError as e:
                raise e
