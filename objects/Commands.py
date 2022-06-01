from abc import abstractmethod
from typing import List, Any, Tuple, Union

from discord import Embed

from objects.Config import Config
from objects.Funds import Funds

config = Config()


class Response:

    def __init__(self,
                 title: str = None,
                 text: str = None,
                 fields: List[Tuple[str, Any]] = None,
                 reaction: str = None):
        self.message = self._format(title, text, fields)
        self.reaction = reaction

    @staticmethod
    def _format(title: str = None,
                text: str = None,
                fields: list = None) -> Union[Embed, None]:
        if title is None and text is None and fields is None:
            return None
        if fields is None:
            fields = list()
        embed = Embed(colour=config.color)
        if title is not None:
            embed.title = title
        if text is not None:
            embed.description = text
        for item in fields:
            key = item[0]
            value = item[1]
            embed.add_field(name=key, value=value, inline=False)
        return embed


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
