from abc import abstractmethod
from typing import List, Any

from objects.Funds import Funds


class Response:

    def __init__(self, text: str):
        self.message = self._format(text)

    @staticmethod
    def _format(text):
        # TODO: Fancy formatting
        return text


class Command:

    @property
    @abstractmethod
    def tags(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def do(self, *args):
        raise NotImplementedError


class Show(Command):

    tags = ['show']

    def __init__(self):
        self._funds = Funds()

    def do(self):
        return Response(text=f'platinum: {self._funds.platinum}\n'
                             f'gold: {self._funds.gold}\n'
                             f'silver: {self._funds.silver}\n'
                             f'copper: {self._funds.copper}\n')


class Plus(Command):

    tags = ['+', 'add', 'plus']

    def __init__(self):
        self._funds = Funds()

    def do(self, amount, currency):
        if currency not in ['platinum', 'gold', 'silver', 'copper']:
            return Response(text=f'Invalid coin type: {currency}')

        print(f'Adding {amount} {currency}...')
        current = getattr(self._funds, currency)
        setattr(self._funds, currency, current + int(amount))

        self._funds.save()
        return Response(text='Done!')


AVAILABLE: List[Any] = [Show, Plus]
