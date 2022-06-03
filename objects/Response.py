from typing import List, Tuple, Any, Union

from discord import Embed

from objects.Config import Config

config = Config()


class Response:

    def __init__(self,
                 title: str = None,
                 text: str = None,
                 fields: List[Tuple[str, Any]] = None,
                 reaction: str = None,
                 url: str = None,
                 icon: str = None):
        self.message = self._format(title, text, fields, url, icon)
        self.reaction = reaction

    @staticmethod
    def _format(title: str = None,
                text: str = None,
                fields: list = None,
                url: str = None,
                icon: str = None) -> Union[Embed, None]:
        if title is None and text is None and fields is None and url is None:
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
        if url is not None:
            embed.url = url
        if icon is not None:
            embed.set_thumbnail(url=icon)
        return embed
