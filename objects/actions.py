from abc import abstractmethod, ABC
from typing import List, Any, Union

from discord import Guild, TextChannel

from coins import Coins, CoinError
from objects.Funds import Funds
from objects.Response import Response


class Action:

    def __init__(self, source: Union[Guild, TextChannel]):
        self.__source = source

    @property
    @abstractmethod
    def tag(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def do(self, *args):
        raise NotImplementedError


class FundedAction(Action, ABC):
    def __init__(self, source: Union[Guild, TextChannel]):
        super().__init__(source)
        self._source = source
        self._funds = Funds(source)


class Show(FundedAction):

    tag = 'show'

    def do(self) -> Response:
        return Response(title='Current funds!',
                        text=f'**platinum:** {self._funds.platinum}\n'
                             f'**gold:** {self._funds.gold}\n'
                             f'**silver:** {self._funds.silver}\n'
                             f'**copper:** {self._funds.copper}\n')


class Plus(FundedAction):

    tag = '+'

    def do(self, amount, currency) -> Response:
        try:
            coin = Coins.get_unit(alias=currency)
        except CoinError as e:
            return Response(title='Error!',
                            text=f'{e}')

        print(f'{self._source.id}: Adding {amount} {coin.name}')
        current = getattr(self._funds, coin.name)
        setattr(self._funds, coin.name, current + int(amount))

        print(f'{self._source.id}: Saving: {self._funds.to_dict()}')
        self._funds.save()
        return Response(reaction='👍')


class Minus(FundedAction):

    tag = '-'

    def do(self, amount, currency) -> Response:
        try:
            coin = Coins.get_unit(alias=currency)
        except CoinError as e:
            return Response(title='Error!',
                            text=f'{e}')

        print(f'{self._source.id}: Removing {amount} {coin.name}')
        current = getattr(self._funds, coin.name)
        setattr(self._funds, coin.name, current - int(amount))

        print(f'{self._source.id}: Saving: {self._funds.to_dict()}')
        self._funds.save()
        return Response(reaction='👍')


AVAILABLE: List[Any] = [Show, Plus, Minus]
