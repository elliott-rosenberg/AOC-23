def solvePart1(file):
    return None

def solvePart2(file):
    return None

def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/08/input1.txt")
