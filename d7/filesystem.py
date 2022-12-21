FILENAME = "test.input"

def generate_list():
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n")
        return reader


class Directory:
    name: str
    size: int
    contents: list

    def __init__(self, name: str) -> None:
        self.name = name
        self.size = 0
        self.contents = []

    def add_child(self, child: object) -> None:
        self.contents.append(child)

    def get_size(self) -> int:
        return self.size

    def calc_size(self) -> int:
        size = 0
        if (len(self.contents) <= 1):
            self.size = size
            return size
        else:
            for x in self.contents:
                child_size = x.get_size()
                if (isinstance(x, Directory)):
                    size += x.calc_size()
                else:
                    size += child_size
            self.size = size
            return size


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size


def part_one():
    terminal_output = generate_list()
    dir_list = []
    pass


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()