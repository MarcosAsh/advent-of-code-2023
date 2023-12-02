from pathlib import Path
import re

gameRegex = re.compile(r"Game (\d+): (.*)$")
color_regex = re.compile(r"(\d+) (.*)")
limits = {"red": 12, "green": 13, "blue": 14}


def part1(line):
    match = gameRegex.search(line)
    for color in match[2].replace(";", ",").split(", "):
        color_match = color_regex.search(color)
        if int(color_match[1]) > limits[color_match[2]]:
            return 0

    return int(match[1])


def part2(line):
    match = gameRegex.search(line)
    rgb = {"red": 0, "green": 0, "blue": 0}
    for color in match[2].replace(";", ",").split(", "):
        color_match = color_regex.search(color)
        value = int(color_match[1])
        color = color_match[2]
        if value > rgb[color]:
            rgb[color] = value

    return rgb["red"] * rgb["green"] * rgb["blue"]


# Open data.txt file
path = Path(__file__).parent / "input day 2.txt"
with path.open() as f:
    # Read all lines
    lines = f.readlines()
    result = [part1(line) for line in lines]
    print("part1: ", sum(result))
    result = [part2(line) for line in lines]
    print("part2: ", sum(result))
