def main():
    with open("inputs/day-5.txt", "r") as file:
        input = file.read()

        part_one(input)
        part_two(input)


def part_one(input: str):
    wrong_updates = []

    splitted_input = input.split("\n\n")

    orderings = [element.split("|")
                 for element in splitted_input[0].split("\n")]
    updates = [element.split(",")
               for element in splitted_input[1].split("\n")]

    for update in updates:
        for rule in orderings:
            if (rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1])):
                wrong_updates.append(update)

    result = sum(int(update[int(len(update) / 2)])
                 for update in updates if update not in wrong_updates)
    print(f"Part 1: {int(result)}")


def part_two(input: str):
    wrong_updates: list[list] = []

    splitted_input = input.split("\n\n")

    orderings = [element.split("|")
                 for element in splitted_input[0].split("\n")]
    updates = [element.split(",")
               for element in splitted_input[1].split("\n")]

    for update in updates:
        for rule in orderings:
            if (rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]) and update not in wrong_updates):
                wrong_updates.append(update)

    for update in wrong_updates:
        for rule in orderings:
            if (rule[0] in update and rule[1] in update):
                while (update.index(rule[0]) > update.index(rule[1])):
                    index = update.index(rule[1])
                    temp = update[index + 1]
                    update[index + 1] = update[index]
                    update[index] = temp

    result = sum(int(update[int(len(update) / 2)])
                 for update in wrong_updates)
    print(f"Part 2: {result}")
    # 5946 is to high

if __name__ == "__main__":
    main()
