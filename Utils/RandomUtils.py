import random


def generate_unique_random_numbers(start, end, count):
    numbers = set()

    while len(numbers) < count:
        number = random.randint(start, end)
        numbers.add(number)

    return list(numbers)
