FILENAME = "calories.input"


def generate_list():
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n\n")
        elf_list = []
        for i in range(len(reader)):
            elf_list.append(reader[i].split("\n"))
    return elf_list


def part_one():
    most_calories = 0
    elf_list = generate_list()

    for x in elf_list:
        y = [int(i) for i in x]
        curr_calories = sum(y)
        if curr_calories > most_calories:
            most_calories = curr_calories

    print(most_calories)


def part_two():
    elf_list = generate_list()
    elf_calories = []
    for x in elf_list:
        y = [int(i) for i in x]
        elf_calories.append(sum(y))
    elf_calories.sort(reverse=True)

    print(sum(elf_calories[0:3]))



if __name__ == "__main__":
    part_one()
    part_two()
