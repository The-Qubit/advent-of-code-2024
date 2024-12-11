def main():
    with open("inputs/day-1.txt", "r") as file:
        input = file.read()

        part_one(input)
        part_two(input)


def part_one(input: str):
    first = []
    second = []

    input_list = input.split("\n")

    for entry in input_list:
        raw_numbers = entry.split("   ")
        first.append(int(raw_numbers[0]))
        second.append(int(raw_numbers[1]))

    first.sort()
    second.sort()
    distances = []

    for i in range(len(first)):
        distances.append(abs(first[i] - second[i]))

    print(f"Part 1: {sum(distances)}")


def part_two(input: str):
    first = []
    second = []

    input_list = input.split("\n")

    for entry in input_list:
        raw_numbers = entry.split("   ")
        first.append(int(raw_numbers[0]))
        second.append(int(raw_numbers[1]))

    first.sort()
    second.sort()
    values = {}

    for i in range(len(first)):
        values[first[i]] = second.count(first[i])

    sum = 0
    for key in values:
        sum += key * values[key]

    print(f"Part 2: {sum}")


if __name__ == "__main__":
    main()
