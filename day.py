from abc import ABC, abstractmethod


def read_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        data = file.readlines()
    return [d.strip() for d in data]


# class for running part 1 and part 2
class Day(ABC):
    # reads a files lines into a list of strings

    @abstractmethod
    def part_1(self):
        return NotImplemented

    @abstractmethod
    def part_2(self):
        return NotImplemented

    def run(self):
        self.part_1()
        self.part_2()
        return
