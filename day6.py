def get_input() -> list[str]:
    with open('day6_input.txt', 'r') as f:
        res = f.readlines()
        res = [i.strip(' \n\r') for i in res]
        return [i for i in res if i != '']
    

def parse_input(lines: list[str]) -> list[(int, int)]:
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    times = (int(i) for i in times)
    distances = (int(i) for i in distances)

    return zip(times, distances)


def find_winning_times(time: int, min_distance: int) -> int:
    #Total number of possible combinations
    count = 0 

    for boost_time in range(1, time):
        travel_time = time - boost_time

        distance = boost_time * travel_time

        if distance > min_distance:
            count += 1

    return count


if __name__ == "__main__":
    lines = get_input()

    data = parse_input(lines)

    res = 1
    for pair in data:
        res *= find_winning_times(pair[0], pair[1])
        print(pair, res)

    print(res)