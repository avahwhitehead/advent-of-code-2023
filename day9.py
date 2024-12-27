import math as maths
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
    inc = seq[-1]
    while True:
        diffs = calculate_differences(seq)
        inc += diffs[-1]
        if is_all_zero(diffs):
            return inc
        
        seq = diffs


def predict_prev_sequence_value(seq: list[int]) -> int:
    diff = [seq[0]]
    while True:
        diffs = calculate_differences(seq)
        diff.insert(0, diffs[0])

        if is_all_zero(diffs):
            s = 0
            for i in range(len(diff)):
                s = diff[i] - s
            return s
        
        seq = diffs


if __name__ == "__main__":
    IS_PUZZLE_2 = True

    lines = get_input()

    lines = parse_input(lines)

    if not IS_PUZZLE_2:
        values_total = 0

        for line in lines:
            next_val = predict_next_sequence_value(line)

            values_total += next_val

        print(values_total)

    else:
        values_total = 0

        for line in lines:
            print(line)
            prev_value = predict_prev_sequence_value(line)

            values_total += prev_value
            print(prev_value)

        print(values_total)
