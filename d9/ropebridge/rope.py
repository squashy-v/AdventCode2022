from __future__ import annotations
from copy import copy


class Knot:
    x: int
    y: int
    point: tuple

    def __init__(self, **kwargs) -> None:
        if "x" in kwargs and "y" in kwargs:
            self.x = kwargs["x"]
            self.y = kwargs["y"]
        elif "point" in kwargs:
            point = kwargs["point"]
            self.x = point[0]
            self.y = point[1]
        else:
            raise ValueError("Knot must be initialized with x and y or tuple")

        self.point = (self.x, self.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"ropebridge.Knot(x={self.x}, y={self.y})"

    def __sub__(self, other) -> Knot:
        return Knot(self.x - other.x, self.y - other.y)

    def move_knot(self, vector: tuple) -> Knot:
        self.x += vector[0]
        self.y += vector[1]
        return self


class Rope:
    length: int
    head: Knot
    tail: Knot
    knot_seq: tuple

    def __init__(self, len: int, head: Knot) -> None:
        self.length = len
        self.knot_seq = tuple(copy(head) for i in range(len))
        self.head = self.knot_seq[0]
        self.tail = self.knot_seq[-1]

    def __str__(self) -> str:
        result: str = ""
        for knot in self.knot_seq:
            result += f"({knot.x}, {knot.y})."
        result = result[:-1]
        return result

    def __repr__(self) -> str:
        print("Object cannot be recreated from __repr__, the internal state will be lost.")
        return f"ropebridge.Rope({self.length}, {self.head.__repr__()})"

    def __iter__(self):
        return iter(self.knot_seq)

    def __next__(self):
        return next(self.knot_seq)

    def __getitem__(self, index: int) -> Knot:
        return self.knot_seq[index]

