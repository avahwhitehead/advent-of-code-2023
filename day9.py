import math as maths
import re
from typing import Self

def get_input() -> list[str]:
    with open('day9_input.txt', 'r') as f:
        res = f.readlines()
        res = [i.strip(' \n\r') for i in res]
        return [i for i in res if i != '']
    

def parse_input(lines: list[str]) -> list[list[int]]:
    lines = [[int(i) for i in line.split()] for line in lines]

    return lines


def calculate_differences(seq: list[int]):
    diff = []
    for i in range(len(seq) - 1):
        diff += [seq[i + 1] - seq[i]]
    return diff


def is_all_zero(seq: list[int]) -> bool:
    return all(i == 0 for i in seq)


def predict_next_sequence_value(seq: list[int]) -> int:
    initial_seq = seq

    inc = 0
    while True:
        diffs = calculate_differences(seq)
        inc += diffs[-1]
        if is_all_zero(diffs):
            return inc + initial_seq[-1]
        
        seq = diffs


if __name__ == "__main__":
    lines = get_input()

    lines = parse_input(lines)

    values_total = 0

    for line in lines:
        next_val = predict_next_sequence_value(line)

        values_total += next_val

    print(values_total)

