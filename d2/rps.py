FILENAME = "rps.input"

def generate_list():
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n")
        round_list = []
        for x in reader:
            round_list.append(x.split(" "))
    return round_list


def determine_round(round: list) -> int:
    if ((round[0] == "A" and round[1] == "Y") or (round[0] == "B" and round[1] == "Z") or (round[0] == "C" and round[1] == "X")):
        return 6
    elif ((round[0] == "A" and round[1] == "Z") or (round[0] == "B" and round[1] == "X") or (round[0] == "C" and round[1] == "Y")):
        return 0
    elif ((round[0] == "A" and round[1] == "X") or (round[0] == "B" and round[1] == "Y") or (round[0] == "C" and round[1] == "Z")):
        return 3

def determine_score(round: list) -> int:
    sum = determine_round(round)
    if round[1] == "X":
        sum += 1
    if round[1] == "Y":
        sum += 2
    if round[1] == "Z":
        sum += 3
    return sum

def get_symbol(round: list) -> str:
    if (round[1] == "X"):
        if round[0] == "A":
            return "Z"
        if round[0] == "B":
            return "X"
        if round[0] == "C":
            return  "Y"
    elif (round[1] == "Y"):
        if round[0] == "A":
            return "X"
        if round[0] == "B":
            return "Y"
        if round[0] == "C":
            return "Z"
    elif (round[1] == "Z"):
        if round[0] == "A":
            return "Y"
        if round[0] == "B":
            return "Z"
        if round[0] == "C":
            return "X"


def part_one():
    stratagy = generate_list()
    score_list = map(determine_score, stratagy)
    print(sum(score_list))


def part_two():
    stratagy = generate_list()
    for x in stratagy:
        x[1] = get_symbol(x)
    score_list = map(determine_score, stratagy)
    print(sum(score_list))


if __name__ == "__main__":
    part_one()
    part_two()