import math as maths

def getInput() -> list[str]:
    with open('day3_input.txt', 'r') as f:
        res = f.readlines()
        res = [i.strip(' \n\r') for i in res]
        return [i for i in res if i != '']

def parseLine(line: str) -> list[str or int or None]:
    numbers = [str(i) for i in range(10)]
    
    consecutive = 0
    currVal = None
    res = []

    for i, v in enumerate(line):
        if v in numbers:
            consecutive += 1
            if currVal is None:
                currVal = 0
            currVal = (currVal * 10) + int(v)
            
            if i < len(line) - 1:
                continue
    
        if consecutive > 0:
            for i in range(consecutive):
                res.append(currVal)
            currVal = None
            consecutive = 0

        if v == '.':
            res.append(None)
        elif v not in numbers:
            res.append(v)

    return res

def parseDiagram(diagram: list[str]) -> list[list[str or int or None]]: 
    return [parseLine(l) for l in diagram]

def getAdjacentParts(diagram: list[list[str or int or None]], row: int, col: int) -> set[int]:
    partnos = list[int]()

    indexes = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1],
    ]

    d = {}

    for [r, c] in indexes:
        if r >= len(diagram):
            continue
        if c >= len(diagram[r]):
            continue

        if not isinstance(diagram[r][c], int):
            continue
        
        if r not in d or d[r] != diagram[r][c]:
            partnos.append(diagram[r][c])
            d[r] = diagram[r][c]

    return partnos

def sumPartNumbers(diagram: list[list[str or int or None]]) -> int:
    s = 0

    parts = list[int]()

    for r, row in enumerate(diagram):
        for c, v in enumerate(row):
            if isinstance(v, int) or v is None:
                continue

            adj = getAdjacentParts(diagram, r, c)
            s += sum(adj)
            for p in adj:
                parts.append(p)

    return sum(parts)
    return partnos

def sumGearRatios(diagram: list[list[str or int or None]]) -> int:
    s = 0

    for r, row in enumerate(diagram):
        for c, v in enumerate(row):
            if v != '*':
                continue

            adj = getAdjacentParts(diagram, r, c)
            if len(adj) != 2:
                continue
            
            s += maths.prod(adj)

    return s


if __name__ == "__main__":
    IS_PUZZLE_2 = True

    inp = getInput()
    diagram = parseDiagram(inp)

    if not IS_PUZZLE_2:
        res = sumPartNumbers(diagram)
    else:
        res = sumGearRatios(diagram)

    print(res)