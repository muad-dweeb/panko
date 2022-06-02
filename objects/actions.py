from abc import abstractmethod
from typing import List, Any

from coins import Coins, CoinError
from objects.Funds import Funds
from objects.Response import Response


class Action:

    @property
    @abstractmethod
    def tag(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def do(self, *args):
        raise NotImplementedError


class Show(Action):

    tag = 'show'

    def __init__(self):
        self._funds = Funds()

    def do(self) -> Response:
        return Response(title='Current funds!',
                        text=f'**platinum:** {self._funds.platinum}\n'
                             f'**gold:** {self._funds.gold}\n'
                             f'**silver:** {self._funds.silver}\n'
                             f'**copper:** {self._funds.copper}\n')


class Plus(Action):

    tag = '+'

    def __init__(self):
        self._funds = Funds()

    def do(self, amount, currency) -> Response:
        try:
            coin = Coins.get_unit(alias=currency)
        except CoinError as e:
            return Response(title='Error!',
                            text=f'{e}')

        print(f'Adding {amount} {coin.name}...')
        current = getattr(self._funds, coin.name)
        setattr(self._funds, coin.name, current + int(amount))

        self._funds.save()
        return Response(reaction='👍')


class Minus(Action):

    tag = '-'

    def __init__(self):
        self._funds = Funds()

    def do(self, amount, currency) -> Response:
        try:
            coin = Coins.get_unit(alias=currency)
        except CoinError as e:
            return Response(title='Error!',
                            text=f'{e}')

        print(f'Removing {amount} {coin.name}...')
        current = getattr(self._funds, coin.name)
        setattr(self._funds, coin.name, current - int(amount))

        self._funds.save()
        return Response(reaction='👍')


AVAILABLE: List[Any] = [Show, Plus, Minus]
