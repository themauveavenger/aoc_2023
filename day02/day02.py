from day import read_file
import operator
import functools
import re

colors = ["green", "blue", "red"]


class GameSet:
    def __init__(self, game_set_str: str):
        self.cube_counts = {
            "green": 0,
            "blue": 0,
            "red": 0
        }
        self.parse_set(game_set_str)

    def parse_set(self, game_set_str: str):
        for color in colors:
            re_pattern = "(\\d{1,3}) " + color
            cube_count = re.search(re_pattern, game_set_str)
            if cube_count is not None:
                self.cube_counts[color] = int(cube_count.group(1))


class Game:
    def __init__(self, game_id: int, game_sets: list[GameSet]):
        self.game_id = game_id
        self.game_sets = game_sets

    def max_color(self, color: str) -> int:
        return max([s.cube_counts[color] for s in self.game_sets])

    def power_of_min_set_cubes(self) -> int:
        max_colors = [self.max_color(color) for color in colors]
        return functools.reduce(operator.mul, max_colors, 1)


# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
def parse_game_line(line: str) -> [int, list[GameSet]]:
    # determine game id
    # split rest of string by semicolons
    # split each set by comma
    # pluck number and color

    # game id
    g_id = int(re.search("Game (\\d{1,3})", line).group(1))

    # split by semicolons
    game_set_lines = line.split(";")

    g_sets = [GameSet(s) for s in game_set_lines]

    return g_id, g_sets


def part_1():
    game_lines = read_file("./day02/input.txt")

    color_totals = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total_game_ids = 0
    for game_line in game_lines:
        game_id, game_sets = parse_game_line(game_line)

        possible = True
        for color in colors:
            for s in game_sets:
                if s.cube_counts[color] > color_totals[color]:
                    possible = False

        if possible:
            total_game_ids += game_id

    print(total_game_ids)


def part_2():
    game_lines = read_file("./day02/input.txt")
    sum_power = 0

    for game_line in game_lines:
        game_id, game_sets = parse_game_line(game_line)

        game = Game(game_id, game_sets)
        power = game.power_of_min_set_cubes()

        sum_power += power

    print(sum_power)


part_1()
part_2()
