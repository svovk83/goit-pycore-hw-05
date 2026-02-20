import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\d+\.\d+|\d+"
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))


if __name__ == "__main__":
    text = "Прибуток склав 100.50, а витрати 50.25."
    print(sum_profit(text, generator_numbers))