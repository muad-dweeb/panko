from abc import abstractmethod
from typing import List, Any

from objects.Funds import Funds
from objects.Response import Response


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

    def do(self) -> Response:
        return Response(title='Current funds!',
                        text=f'**platinum:** {self._funds.platinum}\n'
                             f'**gold:** {self._funds.gold}\n'
                             f'**silver:** {self._funds.silver}\n'
                             f'**copper:** {self._funds.copper}\n')


class Plus(Command):

    tags = ['+', 'add', 'plus']

    def __init__(self):
        self._funds = Funds()

    def do(self, amount, currency) -> Response:
        if currency not in ['platinum', 'gold', 'silver', 'copper']:
            return Response(title='Error!',
                            text=f'Invalid coin type: {currency}')

        print(f'Adding {amount} {currency}...')
        current = getattr(self._funds, currency)
        setattr(self._funds, currency, current + int(amount))

        self._funds.save()
        return Response(reaction='👍')


AVAILABLE: List[Any] = [Show, Plus]
