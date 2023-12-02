from day import Day, read_file
import re

word_to_number_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

words = list(word_to_number_map.keys())


# convert any number words in the line to their number equivalent
# extract any numbers in the line into a list of numbers
# return the list of numbers in order
def extract_numbers_2(line: str) -> list[int]:
    # look forward through line and find first occurrence of a number
    result: list[int] = [-1] * len(line)
    for word in words:
        indices = [m.start() for m in re.finditer(word, line)]
        for index in indices:
            if index > -1:
                result[index] = word_to_number_map[word]

    # find the digits
    for idx, c in enumerate(line):
        if c.isdigit():
            result[idx] = int(c)

    # remove -1 values & return trimmed array
    return [a for a in result if a > -1]


def extract_numbers(line: str) -> list[int]:
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(int(char))
    return numbers


# for each list of numbers, take the first and last number, make a two-digit number, and add it to the sum.
# if there is only one number, add it to the two-digit number twice. [3] -> 33
# if there are no numbers, skip the line
def get_calibration_sum(numbers: list[list[int]]) -> int:
    total = 0
    for number_li in numbers:
        n = 0
        if len(number_li) == 0:
            continue
        elif len(number_li) == 1:
            n = int(f"{number_li[0]}{number_li[0]}")
        else:
            n = int(f"{number_li[0]}{number_li[-1]}")
        total += n

    return total


class Day01(Day):
    def __init__(self):
        super().__init__()

    def part_1(self):
        # read each line into a list of strings
        data = read_file("./day01/input.txt")

        # for each line of data, extract all numbers in the line into a list of numbers
        # sample: ninetwo2eighttwo
        numbers = []
        for line in data:
            number_li = extract_numbers(line)
            numbers.append(number_li)

        total = get_calibration_sum(numbers)

        print(total)

    def part_2(self):
        # read each line into a list of strings
        data = read_file("./day01/input.txt")

        # for each line of data, extract all numbers in the line into a list of numbers
        # sample: ninetwo2eighttwo
        numbers = []
        for line in data:
            number_li = extract_numbers_2(line)
            numbers.append(number_li)

        total = get_calibration_sum(numbers)

        print(total)


if __name__ == "__main__":
    day = Day01()
    day.run()
