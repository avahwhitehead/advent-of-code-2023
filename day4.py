import re

def getInput() -> list[str]:
    with open('day4_input.txt', 'r') as f:
        res = f.readlines()
        res = [i.strip(' \n\r') for i in res]
        return [i for i in res if i != '']

def parseLine(line: str) -> list[list[int]]:
    res = re.search(r"^Card\s+\d+:\s+([\d\s]+)\s*\|\s*([\d\s]+)$", line)

    desired = res.group(1)
    actual = res.group(2)

    desired = re.split(r"\s+", desired)
    actual = re.split(r"\s+", actual)

    return [
        [int(i) for i in desired if i != ''],
        [int(i) for i in actual if i != '']
    ]

def countWins(desired: list[int], actual: list[int]):
    intersection = set(desired) & set(actual)
    return len(intersection)


def calculateWinnings(lines: list[list[int]]):
    points = 0
    for [desired, actual] in lines:
        wins = countWins(desired, actual)

        if wins > 0:
            points += 2 ** (wins - 1)
        
    return points


if __name__ == "__main__":
    inp = getInput()
    lines = [parseLine(i) for i in inp]
    
    res = calculateWinnings(lines)

    print(res)