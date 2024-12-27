import math as maths
import re
from typing import Self

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

def detect_cycles(f, x0) -> (int, int):
    """Brent's cycle detection algorithm."""
    # lam(da): Length of loop
    # mu: Start index of loop

    # main phase: search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == lam:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length λ
    tortoise = hare = x0
    for _ in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare)
    # The distance between the hare and tortoise is now λ.

    # Next, the hare and tortoise move at same speed until they agree
    mu = 0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
 
    return lam, mu

class GraphState:
    graph: { str: (str, str) }
    steps: list[int]

    def __init__(self, graph: { str: (str, str) }, steps: list[int]) -> None:
        self.graph = graph
        self.steps = steps

    def increment(self, x: (str, int)) -> (str, int):
        (current_node, step_index) = x

        step = self.steps[step_index]

        current_node = self.graph[current_node][step]
        step_index = (step_index + 1) % len(self.steps)
        return (current_node, step_index)

    def can_terminate(self, x: (str, int), end_node: str) -> bool:
        (current_node, step_index) = x
        return current_node[-len(end_node):] == end_node
    

def calculate_steps_to_end(graph: { str: (str, str) }, steps: list[int], start_nodes: list[str], end_node: str) -> int or None:
    state = GraphState(graph, steps)

    loop_lengths = []

    for start_node in start_nodes:
        start_state = (start_node, 0)
    
        f = lambda x: state.increment(x)
        cycles = detect_cycles(f, start_state)

        print(start_node, cycles)

        loop_lengths.append(cycles[0])

    lcm = maths.lcm(*loop_lengths)
    return lcm


if __name__ == "__main__":
    IS_PUZZLE_2 = False

    lines = get_input()

    steps, graph = parse_input(lines)

    steps = [0 if i == 'L' else 1 for i in steps]

    if not IS_PUZZLE_2:
        count = calculate_steps_to_end(graph, steps, ['AAA'], 'ZZZ')

        print()
        print("Steps:", count)
        pass
    else:
        starting_nodes = [k for k in graph.keys() if k[-1:] == 'A']
        
        count = calculate_steps_to_end(graph, steps, starting_nodes, 'Z')
        
        print()
        print("Steps:", count)

