from typing import Callable, Any


class FizzBuzz(object):

    def __init__(self):
        self._actions_map = {}

    def when(self, condition: Callable[[Any], bool], action):
        self._actions_map[condition] = action

    def compute(self, number: int) -> str:
        words = [
            value
            for condition, value in self._actions_map.items()
            if condition(number)
        ]
        return "".join(words) if words else str(number)


def is_divisible_by(divisor: int):
    return lambda dividend: dividend % divisor == 0


def contains_number(to_search: int):
    return lambda searched: str(to_search) in str(searched)


def contains_or_is_divisible_by(number: int):
    return lambda x: contains_number(number)(x) or is_divisible_by(number)(x)


if __name__ == '__main__':
    fizz_buzz = FizzBuzz()
    fizz_buzz.when(contains_or_is_divisible_by(3), "Fizz")
    fizz_buzz.when(contains_or_is_divisible_by(5), "Buzz")

    [
        print(f'{number} => {fizz_buzz.compute(number)}')
        for number in range(1, 21)
    ]
