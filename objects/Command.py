from typing import Any, Dict

from objects.actions import AVAILABLE


class CommandError(BaseException):
    pass


class Command:

    """
    The command provided by the user.
    Format:
        '<operator>[Optional<amount><coin>]'
    Examples:
        'show'
        'help'
        '-42s'
        '+42g'
    """

    valid_action_tags = [a.tag for a in AVAILABLE]

    def __init__(self, cmd: str):
        self.original: str = cmd
        self.__components: Dict[Any] = self.parse(cmd)

    @property
    def action(self) -> str:
        return self.__components['action']

    @property
    def args(self) -> list:
        return self.__components['args']

    @staticmethod
    def parse(cmd_str) -> Dict:
        """
        Deconstruct the input command
        :return:
        """
        parsed = {
            'action': None,
            'args': list()
        }
        for tag in Command.valid_action_tags:

            # Action tag acquired
            if cmd_str.startswith(tag):
                parsed['action'] = tag

            # This is not the droid you are looking for
            else:
                continue

            # Additional args detected
            if len(cmd_str) > len(tag):
                arg_str = cmd_str.strip(tag)
                amount_str = ''
                unit_str = ''

                # This is really stupid validation
                if not arg_str[0].isdigit():
                    raise CommandError(f'Invalid arguments: {arg_str}')
                for char in arg_str:
                    if char.isdigit():
                        amount_str += char
                    else:
                        unit_str += char

                if len(unit_str) == 0:
                    raise CommandError(f'Invalid arguments: {arg_str}')

                # Also really stupid validation
                # This should catch cases where the arg format is not
                #   <amount><unit>
                if amount_str + unit_str != arg_str:
                    raise CommandError(f'Invalid arguments: {arg_str}')

                parsed['args'].append(int(amount_str))
                parsed['args'].append(unit_str)

            if parsed['action'] is not None:
                break

        return parsed
