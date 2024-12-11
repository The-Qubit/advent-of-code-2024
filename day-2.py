def main():
    with open("inputs/day-2.txt", "r") as file:
        input = file.read()

        part_one(input)
        part_two(input)


def part_one(input: str):
    input_list = input.split("\n")

    save_reports = 0

    for entry in input_list:
        splitted = entry.split(" ")

        if (is_ascending(splitted) or is_descending(splitted)):
            save_reports += 1

    print(f"Part 1: {save_reports}")


def part_two(input: str):
    input_list = input.split("\n")

    save_reports = 0

    for entry in input_list:
        splitted = entry.split(" ")

        temp = splitted[:]
        found = False

        for i in range(len(splitted) + 1):
            if (is_ascending(temp)):
                save_reports += 1
                found = True
                break
            temp = splitted[:]
            temp.pop(i - 1)

        splitted.reverse()
        temp = splitted[:]

        for i in range(len(splitted) + 1):
            if (is_ascending(temp) and not found):
                save_reports += 1
                break
            temp = splitted[:]
            temp.pop(i - 1)

    print(f"Part 2: {save_reports}")


def is_descending(list: list):
    for i in range(len(list) - 1):
        if (int(list[i]) < int(list[i+1]) or not is_in_range(int(list[i + 1]), int(list[i]))):
            return False
    return True


def is_ascending(list: list):
    for i in range(len(list) - 1):
        if (int(list[i]) > int(list[i+1]) or not is_in_range(int(list[i]), int(list[i + 1]))):
            return False
    return True


def is_in_range(first, second):
    difference = second - first
    if (difference <= 3 and difference >= 1):
        return True
    return False


if __name__ == "__main__":
    main()
