from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 20
        b = 10
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 200
        assert result == expected

    def test_divide(self):
        # arrange
        a = 20
        b = 4
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 5.0
        assert result == expected



    