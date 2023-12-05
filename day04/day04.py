from day import read_file
import math


def part_1():
    data = read_file("./day04/input.txt")
    # remove up to first colon & split on |
    total = 0
    for line in data:
        winning_numbers, your_numbers = line.split(":")[1].strip().split("|")
        winning_numbers = [int(n) for n in winning_numbers.split()]
        your_numbers = [int(n) for n in your_numbers.split()]

        intersection = set(winning_numbers).intersection(your_numbers)

        points = math.floor(math.pow(2, len(intersection) - 1))
        total += points
    print(total)


def main():
    part_1()


main()
