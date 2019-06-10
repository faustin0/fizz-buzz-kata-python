from typing import Callable, Any, Tuple, List


class FizzBuzz(object):

    def __init__(self, actions: List[Tuple] = None):
        self._actions = actions if actions else []

    def when(self, condition: Callable[[Any], bool], action):
        self._actions.append((
            condition, action
        ))

    def compute(self, number):
        words = [
            value
            for condition, value in self._actions
            if condition(number)
        ]
        return "".join(words) if words else str(number)


def is_divisible_by(divisor):
    def inner(dividend):
        return dividend % divisor == 0

    return inner


def contains_number(to_search):
    def inner(searched):
        return str(to_search) in str(searched)

    return inner


if __name__ == '__main__':
    actions = [
        (is_divisible_by(3), "Fizz"),
        (is_divisible_by(5), "Buzz")
    ]
    fizz_buzz = FizzBuzz(actions)
    print([fizz_buzz.compute(number) for number in range(1, 16)])
