from unittest import TestCase

import fizzbuzz
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):

    def mocked_predicate(self, _):
        return True

    def test_should_register_action(self):
        actions = [
            (self.mocked_predicate, "Foo")
        ]
        fizz_buzz = FizzBuzz()
        fizz_buzz.when(self.mocked_predicate, "Foo")
        self.assertEqual(fizz_buzz._actions, actions)

    def test_should_return_Foo_when_true_condition(self):
        actions = [
            (self.mocked_predicate, "Foo")
        ]
        fizz_buzz = FizzBuzz(actions)

        self.assertEqual("Foo", fizz_buzz.compute(3))

    def test_should_contain_number(self):
        contains_five = fizzbuzz.contains_number(5)
        self.assertTrue(contains_five(11511))

    def test_should_not_contain_number(self):
        contains_five = fizzbuzz.contains_number(5)
        self.assertFalse(contains_five(11011))

    def test_should_be_divisible_by(self):
        divisible_by_five = fizzbuzz.is_divisible_by(3)
        self.assertTrue(divisible_by_five(15))

    def test_should_not_be_divisible_by(self):
        divisible_by_five = fizzbuzz.is_divisible_by(3)
        self.assertFalse(divisible_by_five(17))
