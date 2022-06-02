from typing import List, Any, Union


class Copper:
    name = 'copper'
    aliases = ['c', 'cp']
    value = 1


class Silver:
    name = 'silver'
    aliases = ['s', 'sp']
    value = 10


class Gold:
    name = 'gold'
    aliases = ['g', 'gp']
    value = 100


class Platinum:
    name = 'platinum'
    aliases = ['p', 'pp']
    value = 1000


class CoinError(BaseException):
    pass


class Coins:
    available: List[Any] = [Copper, Silver, Gold, Platinum]

    @classmethod
    def aliases(cls) -> List[str]:
        response = list()
        alias_lists = [c.aliases for c in cls.available]
        for item in alias_lists:
            response.extend(item)
        return response

    @classmethod
    def get_unit(cls, alias: str) -> Union[Copper, Silver, Gold, Platinum]:
        if alias not in cls.aliases():
            raise CoinError(f'Invalid coin type: {alias}')
        for coin in cls.available:
            if alias == coin.name or alias in coin.aliases:
                return coin
