from typing import List, Tuple, Any, Union

from discord import Embed

from objects.Config import Config

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