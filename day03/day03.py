from day import read_file


def is_symbol(char: str) -> bool:
    return not char.isdigit() and not char == "."


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, data: list[list[str]]):
        self.data = data

    def get_part_number_total(self):
        num_rows = len(self.data)
        num_cols = len(self.data[0]) if num_rows > 0 else 0

        total = 0
        row = 0
        col = 0
        while row < num_rows:
            while col < num_cols:
                value = self.data[row][col]
                if value.isdigit():
                    # we might have a part number
                    # find out where the number ends
                    next_col_index = col + 1
                    adjacent_values = self.get_adjacent_values(row, col)
                    while next_col_index < num_cols and self.data[row][next_col_index].isdigit() is True:
                        # also get the adjacent values for the next numbers
                        adjacent_values += self.get_adjacent_values(row, next_col_index)
                        value += self.data[row][next_col_index]
                        next_col_index += 1
                    the_number = int(value)

                    # if any of these are a symbol, the number is a part number
                    is_part_number = any([av for av in adjacent_values if is_symbol(av)])
                    if is_part_number is True:
                        total += the_number

                    # advance column index to next non-number space
                    col += len(value)
                else:
                    col += 1

            # set the indices for the next loop
            col = 0
            row += 1

        return total

    # get adjacent values given a current position at row & col
    def get_adjacent_values(self, row: int, col: int):
        adjacent_values = []

        # Check top
        if row > 0:
            adjacent_values.append(self.data[row - 1][col])

        # Check bottom
        if row < len(self.data) - 1:
            adjacent_values.append(self.data[row + 1][col])

        # Check left
        if col > 0:
            adjacent_values.append(self.data[row][col - 1])

        # Check right
        if col < len(self.data[0]) - 1:
            adjacent_values.append(self.data[row][col + 1])

        # Check top-left
        if row > 0 and col > 0:
            adjacent_values.append(self.data[row - 1][col - 1])

        # Check top-right
        if row > 0 and col < len(self.data[0]) - 1:
            adjacent_values.append(self.data[row - 1][col + 1])

        # Check bottom-left
        if row < len(self.data) - 1 and col > 0:
            adjacent_values.append(self.data[row + 1][col - 1])

        # Check bottom-right
        if row < len(self.data) - 1 and col < len(self.data[0]) - 1:
            adjacent_values.append(self.data[row + 1][col + 1])

        return adjacent_values


def part_1():
    # read in the file
    data = read_file("./day03/input.txt")
    # convert lines to list[list[str]]
    lines = [[c for c in line] for line in data]

    grid = Grid(lines)
    print(grid.get_part_number_total())


def part_2():
    data = read_file("./day03/input.txt")
    # convert lines to list[list[str]]
    lines = [[c for c in line] for line in data]

    grid = Grid(lines)


def main():
    part_1()
    part_2()


main()
