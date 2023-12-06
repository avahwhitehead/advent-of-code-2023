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
    

def calculateWinnings2(lines: list[list[int]]):
    # Store the number of each following card
    # Including the original and duplicates
    following_card_counts = []

    total_card_count = 0
    for [desired, actual] in lines:
        if len(following_card_counts) == 0:
            # No explicit number defined - only 1 card (no copies)
            curr_card_count = 1
        else:
            # Use the provided number of cards
            curr_card_count = following_card_counts[0]
            following_card_counts = following_card_counts[1:]

        #Count the number of wins in the current card
        wins = countWins(desired, actual)

        # 1 more copy of the next #`wins` cards
        # For each copy of this card
        for j in range(wins):
            # Add the count of the current card to the number of copies of the upcoming cards
            if j < len(following_card_counts):
                # Already has a count - just add these copies
                following_card_counts[j] += curr_card_count
            else:
                # No count yet - add these copies, and count the original
                following_card_counts.append(curr_card_count + 1)

        # Add the current number of cards to the total
        total_card_count += curr_card_count

    return total_card_count


if __name__ == "__main__":
    IS_PUZZLE_2 = True

    inp = getInput()
    lines = [parseLine(i) for i in inp]
    
    if not IS_PUZZLE_2:
        res = calculateWinnings(lines)
    else:
        res = calculateWinnings2(lines)

    print(res)