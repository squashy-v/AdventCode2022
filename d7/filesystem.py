from __future__ import annotations
FILENAME = "filesystem.input"


def generate_list():
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().split("\n")
        while "$ cd .." in reader:
            reader.remove("$ cd ..")
        while "$ ls" in reader:
            reader.remove("$ ls")
        return reader


class Directory:
    name: str
    size: int
    contents: list

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.size: int = 0
        self.contents: list = []

    def add_child(self, child: object) -> None:
        self.contents.append(child)

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def get_contents(self) -> list:
        return self.contents

    def calc_size(self) -> int:
        size = 0
        if (len(self.contents) < 1):
            self.size = size
            return size
        else:
            for x in self.contents:
                if (isinstance(x, Directory)):
                    size += x.calc_size()
                else:
                    child_size = x.get_size()
                    size += child_size
            self.size = size
            return size

    def find_child(self, child: str) -> Directory:
        for x in self.contents:
            if (isinstance(x, Directory)):
                if x.get_name() == child:
                    return x
                else:
                    result = x.find_child(child)
                    if isinstance(result, Directory):
                        return result


def dir_under_value(search_base: Directory, size: int) -> list:
    result: list = []
    for x in search_base.get_contents():
        if (isinstance(x, Directory)):
            if x.get_size() <= size:
                result.append(x)
            result.extend(dir_under_value(x, size))
    return result


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int) -> None:
        self.name: str = name
        self.size: int = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size


def part_one() -> Directory:
    terminal_output = generate_list()
    terminal_output.pop(0)
    root: Directory = Directory("/")
    cwd: Directory = root

    for i in terminal_output:
        if "$ cd" in i:
            new_cwd: str = i.replace("$ cd ", "")
            cwd = root.find_child(new_cwd)

        if "dir" in i:
            new_dir: str = i.replace("dir ", "")
            cwd.add_child(Directory(new_dir))

        if i[0].isnumeric():
            new_file = i.split(" ")
            cwd.add_child(File(new_file[1], int(new_file[0])))

    root.calc_size()
    targets = dir_under_value(root, 100000)
    targets = [x.size for x in targets]
    print(sum(targets))
    return root


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()
