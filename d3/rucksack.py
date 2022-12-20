from string import ascii_letters
FILENAME = "rucksack.input"
PRIODICT = list(enumerate(ascii_letters, 1))

def generate_list(do_split):
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n")
        rucksack_list = []
        if do_split:
            for i in range(len(reader)):
                cut = int(len(reader[i])/2)
                new_list = [reader[i][0:cut], reader[i][cut:]]
                rucksack_list.append(new_list)
        else:
            rucksack_list = reader
    return rucksack_list

def return_prio(x: str) -> int:
    for i in PRIODICT:
        if i[1] == x:
            return i[0]

def part_one():
    rucksack_list = generate_list(True)
    dupe_items = []
    for rucksack in rucksack_list:
        for x in rucksack[0]:
            if (x in rucksack[1]):
                dupe_items.append(x)
                break
    item_prio_list = map(return_prio, dupe_items)
    print(sum(item_prio_list))
    


def part_two():
    rucksack_list = generate_list(False)
    groups_list = [rucksack_list[i:i+3] for i in range(0, len(rucksack_list), 3)]
    badge_list = []
    for group in groups_list:
        for x in group[0]:
            if (x in group[1]) and (x in group[2]):
                badge_list.append(x)
                break
    badge_prio_list = map(return_prio, badge_list)
    print(sum(badge_prio_list))



if __name__ == "__main__":
    part_one()
    part_two()
