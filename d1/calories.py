#!/usr/bin/env python
FILENAME: str = "calories.input"


def generate_list() -> list:
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n\n")
        elf_list: list = []
        for i in range(len(reader)):
            elf_list.append(reader[i].split("\n"))
    return elf_list


def part_one() -> None:
    most_calories: int = 0
    elf_list: list = generate_list()

    for x in elf_list:
        y: list = [int(i) for i in x]
        curr_calories: int = sum(y)
        if curr_calories > most_calories:
            most_calories = curr_calories

    print(most_calories)


def part_two() -> None:
    elf_list: list = generate_list()
    elf_calories: list = []
    for x in elf_list:
        y = [int(i) for i in x]
        elf_calories.append(sum(y))
    elf_calories.sort(reverse=True)

    print(sum(elf_calories[0:3]))


if __name__ == "__main__":
    part_one()
    part_two()
