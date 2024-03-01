#!/usr/bin/env python
FILENAME: str = "treehouse.input"


def generate_forest() -> list:
    with open(FILENAME, "rt") as file:
        reader = file.read().splitlines()
        reader: list = list(map(list, reader))
    return reader


def gen_temp_vertical(forest: list, index: int) -> list:
    vert_list: list = []
    for x in forest:
        vert_list.append(x[index])
    return vert_list


def tallest_tree(tree: int, row: list, index: int) -> bool:
    visable: bool = True
    first_half: list = row[:index]
    second_half: list = row[index+1:]
    for x in first_half:
        if tree <= x:
            visable = False
    if visable:
        return True
    else:
        visable = True
        for x in second_half:
            if tree <= x:
                visable = False
    return visable


def calc_view(tree: int, row: list, index: int) -> int:
    first_half: list = row[:index]
    second_half: list = row[index+1:]
    count_one: int = 0
    for x in first_half[::-1]:
        if tree > x:
            count_one += 1
        elif tree <= x:
            count_one += 1
            break
    count_two: int = 0
    for x in second_half:
        if tree > x:
            count_two += 1
        elif tree <= x:
            count_two += 1
            break

    return (count_one * count_two)


def part_one() -> None:
    count: int = 0
    forest: list = generate_forest()
    count += (4*len(forest)) - 4
    for i in range(len(forest)):
        if (i == 0) or (i == len(forest) - 1):
            continue
        for j in range(len(forest[i])):
            if (j == 0) or (j == len(forest) - 1):
                continue
            x_list: list = forest[i]
            y_list: list = gen_temp_vertical(forest, j)
            if ((tallest_tree(forest[i][j], x_list, j)) or
                    (tallest_tree(forest[i][j], y_list, i))):
                count += 1

    print(count)


def part_two() -> None:
    highest_value: int = 0
    forest: list = generate_forest()
    for i in range(len(forest)):
        if (i == 0) or (i == len(forest) - 1):
            continue
        for j in range(len(forest[i])):
            if (j == 0) or (j == len(forest) - 1):
                continue
            x_list: list = forest[i]
            y_list: list = gen_temp_vertical(forest, j)
            x_view: int = calc_view(forest[i][j], x_list, j)
            y_view: int = calc_view(forest[i][j], y_list, i)
            curr_view = (x_view * y_view)
            if curr_view > highest_value:
                highest_value = curr_view

    print(highest_value)


if __name__ == "__main__":
    part_one()
    part_two()
