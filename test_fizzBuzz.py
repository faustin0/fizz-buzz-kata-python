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

    def test_should_contains_and_be_divisible_by(self):
        contains_or_is_divisible_by_five = fizzbuzz.contains_or_is_divisible_by(5)
        self.assertTrue(contains_or_is_divisible_by_five(10), msg="expected 10 to be divisible by 5")
        self.assertTrue(contains_or_is_divisible_by_five(51))

    def test_should_not_contains_and_be_divisible_by(self):
        contains_or_is_divisible_by_five = fizzbuzz.contains_or_is_divisible_by(5)
        self.assertFalse(contains_or_is_divisible_by_five(4), msg="expected 4 to be not divisible by 5")
        self.assertFalse(contains_or_is_divisible_by_five(12))

    def test_should_return_fizz(self):
        contains_or_is_divisible_by_three = fizzbuzz.contains_or_is_divisible_by(3)
        sut = fizzbuzz.FizzBuzz()
        sut.when(contains_or_is_divisible_by_three, "fizz")
        self.assertEqual(sut.compute(3), "fizz", msg="expected to compute fizz when is divisible by 3")
        self.assertEqual(sut.compute(13), "fizz", msg="expected to compute fizz when contains 3")

    def test_should_return_buzz(self):
        contains_or_is_divisible_by_five = fizzbuzz.contains_or_is_divisible_by(5)
        sut = fizzbuzz.FizzBuzz()
        sut.when(contains_or_is_divisible_by_five, "buzz")
        self.assertEqual(sut.compute(10), "buzz", msg="expected to compute buzz when is divisible by 5")
        self.assertEqual(sut.compute(51), "buzz", msg="expected to compute buzz when contains 5")
