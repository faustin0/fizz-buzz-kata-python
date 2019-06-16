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
    return lambda dividend: dividend % divisor == 0


def contains_number(to_search):
    return lambda searched: str(to_search) in str(searched)


def contains_or_is_divisible_by(number):
    return lambda x: contains_number(number)(x) or is_divisible_by(number)(x)


if __name__ == '__main__':
    actions = [
        (contains_or_is_divisible_by(3), "Fizz"),
        (contains_or_is_divisible_by(5), "Buzz")
    ]
    fizz_buzz = FizzBuzz(actions)
    [
        print(f'{number} => {fizz_buzz.compute(number)}')
        for number in range(1, 21)
    ]
