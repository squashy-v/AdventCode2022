#!/usr/bin/env python
from __future__ import annotations
FILENAME: str = "filesystem.input"


def generate_list() -> list:
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().splitlines()
        while "$ ls" in reader:
            reader.remove('$ ls')
    return reader


class Directory:
    def __init__(self, path: str) -> None:
        self.size: int = 0
        self.contents: list = []
        self.path = path

    def get_size(self) -> int:
        return self.size

    def get_contents(self) -> list:
        return self.contents

    def get_path(self) -> str:
        return self.path

    def add_child_dir(self, dir: Directory) -> list:
        self.contents.append(dir)
        return self.contents

    def add_child_file(self, size: int) -> int:
        self.size += size
        return self.size

    def calc_size(self) -> int:
        for x in self.contents:
            self.size += x.calc_size()
        return self.size

    def find_child(self, child_path: str) -> Directory:
        result = ""
        for x in self.contents:
            if x.get_path() == child_path:
                result = x
            else:
                result = x.find_child(child_path)
            if (isinstance(result, Directory)):
                return result


def dir_under_value(search_base: Directory, size: int) -> list:
    result: list = []
    for x in search_base.get_contents():
        if x.get_size() <= size:
            result.append(x)
        result.extend(dir_under_value(x, size))
    return result


def dir_over_value(search_base: Directory, size: int) -> list:
    result: list = []
    for x in search_base.get_contents():
        if x.get_size() >= size:
            result.append(x)
        result.extend(dir_over_value(x, size))
    return result


def part_one():
    terminal_output = generate_list()
    terminal_output.pop(0)
    root: Directory = Directory("/")
    cwd: Directory = root
    for i in terminal_output:
        if "$ cd" in i:
            new_cwd: str = i.replace("$ cd ", "")
            if new_cwd == "..":
                new_cwd = cwd.get_path()
                i = new_cwd.rfind("/", 0, -1)
                new_cwd = new_cwd[:i+1]
                if new_cwd == "/":
                    cwd = root
                else:
                    cwd = root.find_child(new_cwd)

            else:
                cwd = root.find_child(cwd.get_path() + new_cwd + "/")

        elif "dir" in i:
            new_dir: str = i.replace("dir ", "")
            cwd.add_child_dir(Directory(cwd.get_path() + new_dir + "/"))

        elif i[0].isnumeric():
            new_file: list = i.split(" ")
            cwd.add_child_file(int(new_file[0]))

    root.calc_size()
    targets = dir_under_value(root, 100000)
    targets = [x.get_size() for x in targets]
    print(sum(targets))
    return root


def part_two(root: Directory):
    size_free = 70000000 - root.get_size()
    size_needed = 30000000 - size_free
    targets = dir_over_value(root, size_needed)
    targets = [x.get_size() for x in targets]
    smallest_to_free = root.get_size()
    for x in targets:
        if (x < smallest_to_free):
            smallest_to_free = x

    print(smallest_to_free)


if __name__ == "__main__":
    root = part_one()
    part_two(root)
