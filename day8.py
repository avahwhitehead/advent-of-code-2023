import math as maths
import re

def get_input() -> list[str]:
    with open('day8_input.txt', 'r') as f:
        res = f.readlines()
        res = [i.strip(' \n\r') for i in res]
        return [i for i in res if i != '']
    

def parse_input(lines: list[str]) -> (list[str], { str: (str, str) }):
    res = {}

    steps = list(lines.pop(0))

    for line in lines:
        node, lr = re.split(r"\s*=\s*", line)
        
        lr_regex = re.search(r"\((\w+),\s*(\w+)\)", lr)

        left = lr_regex.group(1)
        right = lr_regex.group(2)

        res[node] = (left, right)

    return (steps, res)

def count_steps_to_end(graph: { str: (str, str) }, steps: list[str], curr_node: str, end: str) -> int:
    count = 0
    step_index = 0

    while curr_node != end:
        step = steps[step_index]
        if step == 'L':
            step = 0
        else:
            step = 1

        # print(curr_node, step)
        curr_node = graph[curr_node][step]

        step_index = (step_index + 1) % len(steps)
        count += 1

    return count


if __name__ == "__main__":
    lines = get_input()

    steps, graph = parse_input(lines)

    count = count_steps_to_end(graph, steps, 'AAA', 'ZZZ')

    print()
    print("Steps:", count)
