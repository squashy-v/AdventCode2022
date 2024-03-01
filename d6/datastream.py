#!/usr/bin/env python
FILENAME: str = "datastream.input"


def generate_datastream() -> str:
    with open(FILENAME, "rt", encoding="ascii") as input_file:
        reader = input_file.read().strip()
    return reader


def any_dupes(packet: list) -> bool:
    for x in packet:
        if packet.count(x) > 1:
            return True
    else:
        return False


def part_one() -> None:
    datastream: str = generate_datastream()
    curr_packet: list = []
    packet_start: int = 0
    for i in range(len(datastream)):
        if i <= 3:
            curr_packet.append(datastream[i])
        else:
            curr_packet.pop(0)
            curr_packet.append(datastream[i])
            if not any_dupes(curr_packet):
                packet_start = i + 1
                break

    print(curr_packet, packet_start)


def part_two() -> None:
    datastream: str = generate_datastream()
    curr_packet: list = []
    packet_start: int = 0
    for i in range(len(datastream)):
        if i <= 13:
            curr_packet.append(datastream[i])
        else:
            curr_packet.pop(0)
            curr_packet.append(datastream[i])
            if not any_dupes(curr_packet):
                packet_start = i + 1
                break

    print(curr_packet, packet_start)


if __name__ == "__main__":
    part_one()
    part_two()
