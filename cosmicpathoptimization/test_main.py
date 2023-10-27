import unittest
from hypothesis import given
from hypothesis.strategies import lists, integers
from typing import List
from main import mean_temperature, sum_temperature


class TestMain(unittest.TestCase):

    @given(lists(integers(min_value=1, max_value=100), min_size=1),
           integers(min_value=1, max_value=100))
    def test_mean_temperature_normal(
            self,
            temperatures: List[int],
            num_of_readings: int) -> None:
        expected = sum(temperatures) // num_of_readings
        self.assertEqual(
            mean_temperature(
                num_of_readings,
                temperatures),
            expected)

    @given(lists(integers(min_value=-100, max_value=0), min_size=1),
           integers(min_value=1, max_value=100))
    def test_mean_temperature_negative(
            self,
            temperatures: List[int],
            num_of_readings: int) -> None:
        expected = int(sum(temperatures) / num_of_readings)
        self.assertEqual(
            mean_temperature(
                num_of_readings,
                temperatures),
            expected)

    def test_mean_temperature_empty_list(self) -> None:
        self.assertEqual(mean_temperature(0, []), None)

    @given(integers(min_value=-100, max_value=100))
    def test_mean_temperature_single_element(self, temperature: int) -> None:
        self.assertEqual(mean_temperature(1, [temperature]), temperature)

    @given(lists(integers(min_value=1, max_value=100), min_size=1))
    def test_sum_temperature_normal(self, temperatures: List[int]) -> None:
        self.assertEqual(sum_temperature(temperatures), sum(temperatures))

    @given(lists(integers(min_value=-100, max_value=0), min_size=1))
    def test_sum_temperature_negative(self, temperatures: List[int]) -> None:
        self.assertEqual(sum_temperature(temperatures), sum(temperatures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
