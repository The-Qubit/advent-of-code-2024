def main():
    with open("inputs/day-4.txt", "r") as file:
        input = file.read()

        part_one(input)
        part_two(input)


def part_one(input_str: str):
    total_matches = 0

    matrix = input_str.split("\n")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # XMAS horizontally
            if (j < len(matrix[i]) - 3 and matrix[i][j] == "X" and matrix[i][j+1] == "M" and matrix[i][j+2] == "A" and matrix[i][j+3] == "S"):
                total_matches += 1

            # SMAX horizontally
            if (j < len(matrix[i]) - 3 and matrix[i][j] == "S" and matrix[i][j+1] == "A" and matrix[i][j+2] == "M" and matrix[i][j+3] == "X"):
                total_matches += 1

            # XMAS vertically
            if (i < len(matrix) - 3 and matrix[i][j] == "X" and matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S"):
                total_matches += 1

            # SMAX vertically
            if (i < len(matrix) - 3 and matrix[i][j] == "S" and matrix[i+1][j] == "A" and matrix[i+2][j] == "M" and matrix[i+3][j] == "X"):
                total_matches += 1

            # X _> M _> A _> S
            if (i < len(matrix) - 3 and j < len(matrix[i]) - 3 and matrix[i][j] == "X" and matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S"):
                total_matches += 1

            # S _> A _> M _> X
            if (i < len(matrix) - 3 and j < len(matrix[i]) - 3 and matrix[i][j] == "S" and matrix[i+1][j+1] == "A" and matrix[i+2][j+2] == "M" and matrix[i+3][j+3] == "X"):
                total_matches += 1

            # X ^> M ^> A ^> S
            if (i >= 3 and j < len(matrix[i]) - 3 and matrix[i][j] == "X" and matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S"):
                total_matches += 1

            # S ^> A ^> M ^> X
            if (i >= 3 and j < len(matrix[i]) - 3 and matrix[i][j] == "S" and matrix[i-1][j+1] == "A" and matrix[i-2][j+2] == "M" and matrix[i-3][j+3] == "X"):
                total_matches += 1

    print(f"Part 1: {total_matches}")
    # 2480 is to low


def part_two(input_str: str):
    constellations = [
        ["M", "S", "A", "M", "S"],
        ["S", "M", "A", "S", "M"],
        ["M", "M", "A", "S", "S"],
        ["S", "S", "A", "M", "M"],
    ]

    total_matches = 0
    matrix = input_str.split("\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for item in constellations:
                if (i > 0 and j > 0 and i < len(matrix) - 1 and j < len(matrix[i]) - 1 and matrix[i-1][j-1] == item[0] and matrix[i-1][j+1] == item[1] and matrix[i][j] == item[2] and matrix[i+1][j-1] == item[3] and matrix[i+1][j+1] == item[4]):
                    total_matches += 1

    print(f"Part 2: {total_matches}")


if __name__ == "__main__":
    main()
