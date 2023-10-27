from typing import List, Union


def mean_temperature(num_of_readings: int,
                     temperatures: List[int]) -> Union[int, None]:
    if num_of_readings == 0:
        return None
    return int(sum_temperature(temperatures) / num_of_readings)


def sum_temperature(temperatures: List[int]) -> int:
    return sum(temperatures)


def main() -> None:
    num_of_readings: int = int(input())
    temperatures: List[int] = list(map(int, input().split()))
    result: Union[int, None] = mean_temperature(num_of_readings, temperatures)
    print(result)


if __name__ == "__main__":
    main()
