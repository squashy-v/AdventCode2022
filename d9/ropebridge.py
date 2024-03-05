#!/usr/bin/env python
from __future__ import annotations
import numpy as np
FILENAME: str = "ropebridge.input"


def generate_list() -> list:
    with open(FILENAME, "rt") as file:
        reader = file.read().splitlines()
        result = [list(x.split(" ")) for x in reader]
    return result


class RopeBridge:
    head: np.array = np.array([1, 5], dtype=int)
    tail: np.array = np.array([1, 5], dtype=int)
    state: np.ndarray

    def __init__(self, state: np.ndarray) -> None:
        self.state = state
        self.update_state()

    def __str__(self) -> str:
        return f" {self.head=}\n {self.tail=}\n {self.state.__str__()[1:-1]}"

    def get_state(self) -> np.ndarray:
        return self.state

    def move_head(self, direction: str) -> None:
        match direction:
            case "U":
                if self.head[1] == 1:
                    return None
                else:
                    self.head[1] -= 1
            case "D":
                if self.head[1] == 5:
                    return None
                else:
                    self.head[1] += 1
            case "L":
                if self.head[0] == 1:
                    return None
                else:
                    self.head[0] -= 1
            case "R":
                if self.head[0] == 4:
                    return None
                else:
                    self.head[0] += 1

        self.update_tail()

    def move_tail(self, diff: np.array) -> None:
        if diff[0] == 0:
            self.tail[1] += (diff[1] // 2)

        elif diff[1] == 0:
            self.tail[0] += (diff[0] // 2)

        elif abs(diff[0]) == 2:
            self.tail[0] += (diff[0] // 2)
            self.tail[1] += diff[1]

        elif abs(diff[1]) == 2:
            self.tail[0] += diff[0]
            self.tail[1] += (diff[1] // 2)

    def update_tail(self) -> RopeBridge:
        diff = self.head - self.tail
        if (-1 <= diff[0] <= 1) and (-1 <= diff[1] <= 1):
            return self
        else:
            self.move_tail(diff)
            self.update_state()

    def update_state(self) -> None:
        x, y = self.tail - 1
        self.state[y, x] = 1


def part_one() -> None:
    instruction_list: list = generate_list()
    MAT_SIZE: tuple = (5, 6)
    state: np.ndarray = np.zeros(MAT_SIZE, dtype=int)
    bridge = RopeBridge(state)
    for instruction in instruction_list:
        for x in range(int(instruction[1])):
            bridge.move_head(instruction[0])
    print(bridge)
    print(" " + str(np.count_nonzero(bridge.get_state())))


def part_two() -> None:
    pass


if __name__ == "__main__":
    part_one()
    part_two()
