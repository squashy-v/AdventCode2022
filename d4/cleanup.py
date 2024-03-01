#!/usr/bin/env python
FILENAME = "cleanup.input"

def generate_list():
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n")
        elf_assignment = [x.split(',') for x in reader]
        for x in elf_assignment:
            for i in range(len(x)):
                x[i] = x[i].split("-")
        return elf_assignment

def does_contain(x: list, y: list) -> bool:
    if (int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1])):
        return True
    else:
        return False


def any_contain(x: list, y:list) -> bool:
    if (int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[0])):
        return True
    elif (int(x[0]) <= int(y[1]) and int(x[0]) >= int(y[1])):
        return True
    else:
        return False


def part_one():
    elf_assignment = generate_list()
    
    count = 0
    for x in elf_assignment:
        if does_contain(x[0], x[1]):
            count += 1
        elif does_contain(x[1], x[0]):
            count += 1
    print(count)


def part_two():
    elf_assignment = generate_list()
    count = 0
    for x in elf_assignment:
        if any_contain(x[0], x[1]):
            count += 1
        elif any_contain(x[1], x[0]):
            count += 1
    print(count)
    



if __name__ == "__main__":
    part_one()
    part_two()
