#!/usr/bin/env python
FILENAME = "supplies.input"


class CrateStack:
    stack: list
    height: int
    
    def __init__(self) -> None:
        self.stack = []
        self.height = 0

    def add_top(self, ele: str) -> None:
        self.stack.append(ele)
        self.height = len(self.stack)
    
    def pop_top(self) -> str:
        ele = self.stack.pop()
        self.height = len(self.stack)
        return ele

    def return_crate(self, i) -> str:
        return self.stack[i]

    def return_height(self) -> int:
        return self.height


class CrateConfig:
    config: list

    def __init__(self) -> None:
        self.config = []
        if FILENAME == "test.input":
            for x in range(3):
                new_stack = CrateStack()
                self.config.append(new_stack)
        else:
            for x in range(9):
                new_stack = CrateStack()
                self.config.append(new_stack)

    def __str__(self) -> str:
        biggest = 0
        for x in self.config:
            _ = x.return_height()
            if _ > biggest:
                biggest = _

        output = ""
        for i in range(biggest-1, -1, -1):
            for x in self.config:
                if x.return_height() < i+1:
                    output += "[ ]"
                else:
                    output += f"[{x.return_crate(i)}]"
                output += " "
            output += "\n"
        return output

    def add_crate(self, crate: str, i: int) -> None:
        self.config[i].add_top(crate)

    def move_crate(self, here: int, there: int) -> None:
        crate = self.config[here].pop_top()
        self.config[there].add_top(crate)

    def move_crates(self, num: int, here: int, there: int) -> None:
        crate_stack = []
        for x in range(num):
            crate_stack.append(self.config[here].pop_top())
    
        for x in reversed(crate_stack):
            self.config[there].add_top(x)



def generate_list():
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n")
        instruction_list = [x.split(" ")[1:6:2] for x in reader]

    return instruction_list

def create_crates(config: CrateConfig, col: str, i: int) -> None:
    for x in reversed(col):
        config.add_crate(x, i)


def part_one():
    crates= CrateConfig()
    instructions = generate_list()
    if FILENAME == "test.input":
        create_crates(crates, "NZ", 0)
        create_crates(crates, "DCM", 1)
        create_crates(crates, "P", 2)
    else:
        create_crates(crates, "NRJTZBDF", 0)
        create_crates(crates, "HJNSR", 1)
        create_crates(crates, "QFZGJNRC", 2)
        create_crates(crates, "QTRGNVF", 3)
        create_crates(crates, "FQTL", 4)
        create_crates(crates, "NGRBZWCQ", 5)
        create_crates(crates, "MHNSLCF", 6)
        create_crates(crates, "JTMQND", 7)
        create_crates(crates, "SGP", 8)
    # print(crates)
    
    for x in instructions:
        for i in range(int(x[0])):
            crates.move_crate(int(x[1])-1, int(x[2])-1)

    top_layer = ""
    for x in crates.config:
        top_layer += x.return_crate(-1)
    print(top_layer)
    


def part_two():
    crates= CrateConfig()
    instructions = generate_list()
    if FILENAME == "test.input":
        create_crates(crates, "NZ", 0)
        create_crates(crates, "DCM", 1)
        create_crates(crates, "P", 2)
    else:
        create_crates(crates, "NRJTZBDF", 0)
        create_crates(crates, "HJNSR", 1)
        create_crates(crates, "QFZGJNRC", 2)
        create_crates(crates, "QTRGNVF", 3)
        create_crates(crates, "FQTL", 4)
        create_crates(crates, "NGRBZWCQ", 5)
        create_crates(crates, "MHNSLCF", 6)
        create_crates(crates, "JTMQND", 7)
        create_crates(crates, "SGP", 8)
    # print(crates)

    for x in instructions:
        crates.move_crates(int(x[0]), int(x[1])-1, int(x[2])-1)
    
    top_layer = ""
    for x in crates.config:
        top_layer += x.return_crate(-1)
    print(top_layer)


if __name__ == "__main__":
    part_one()
    part_two()