from collections import defaultdict
from functools import reduce
from operator import mul as multiply

CUBES_IN_BAG_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main_1(input_lines: list[str]):

    result_sum = 0
    for line in input_lines:
        game_header, game_content = line.split(":")
        game_idx = int(game_header.split()[1])
        games = game_content.split(";")
        is_game_possible = True
        for game in games:
            game_items = game.split(',')
            for item in game_items:
                count, color = item.split()
                if int(count) > CUBES_IN_BAG_COUNT[color]:
                    is_game_possible = False
                    break
            if not is_game_possible:
                break
        if is_game_possible:
            result_sum += game_idx

    print("Part 1", result_sum)


def main_2(input_lines: list[str]):
    result_sum = 0
    for line in input_lines:
        least_cubes_count = defaultdict(lambda: 0)
        game_header, game_content = line.split(":")
        for game in game_content.split(";"):
            game_items = game.split(',')
            for item in game_items:
                count, color = item.split()
                if int(count) > least_cubes_count[color]:
                    least_cubes_count[color] = int(count)
        result_sum += reduce(multiply, least_cubes_count.values())
    print("Part 2", result_sum)


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        lines = f.readlines()
    main_1(lines)
    main_2(lines)
