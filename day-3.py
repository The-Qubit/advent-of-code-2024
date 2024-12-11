import re


def main():
    with open("inputs/day-3.txt", "r") as file:
        input = file.read()

        part_one(input)
        part_two(input)


def part_one(input: str):
    matches: str = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    numbers = []
    for element in matches:
        numbers.append(element[4:-1].split(","))

    sum = 0
    for element in numbers:
        sum += int(element[0]) * int(element[1])

    print(f"Part 1: {sum}")


def part_two(input_str: str):
    input_str = input_str.replace("\n", "")
    splitted = input_str.split("don't()")
    splitted[0] = "do()" + splitted[0]

    sum = 0
    for element in splitted:
        match = re.search("do()", element)
        if (match is None):
            continue
        span = match.span()
        activated = element[span[1]:]

        matches: str = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", activated)
        numbers = []
        for element in matches:
            numbers.append(element[4:-1].split(","))

        for element in numbers:
            sum += int(element[0]) * int(element[1])

    print(f"Part 2: {sum}")


if __name__ == "__main__":
    main()
