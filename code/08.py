# def solvePart1(file):
#     firstRow = True
#     dirs = ''
#     coords_map = {}
#     for row in file:
#         # print(row)
#         if firstRow:
#             firstRow = False
#             dirs = row
#         else :
#             if len(row) > 1:

#                 source = row.split('=')[0].strip()
#                 dest1 = row.split('=')[1].strip().split(',')[0][1:]
#                 print(dest1)
#                 dest2 = row.split('=')[1].strip().split(',')[1][1:-1]
#                 coords_map[source] = (dest1, dest2)
#     # print(coords_map)
#     zSteps = 0
#     reachedZ = False
#     dirIndex = 0
#     s = 'AAA'
#     while (not reachedZ):
#         zSteps += 1
#         direction = dirs[dirIndex % len(dirs)]
#         dirIndex += 1

#         if (direction == 'L'):
#             s = coords_map[s][0]
#         else:
#             s = coords_map[s][1]
#         if s == 'ZZZ':
#             break
        

#     return zSteps

# def solvePart2(file):
#     firstRow = True
#     dirs = ''
#     coords_map = {}
#     for row in file:
#         if firstRow:
#             firstRow = False
#             dirs = row
#         else :
#             if len(row) > 1:

#                 source = row.split('=')[0].strip()
#                 dest1 = row.split('=')[1].strip().split(',')[0][1:]
#                 dest2 = row.split('=')[1].strip().split(',')[1][1:-1]
#                 coords_map[source] = (dest1, dest2)
#     sources = []
#     for coord in coords_map.keys():
#         if coord[-1] == 'A':
#             sources.append(coord)

    
#     zSteps = 0
#     reachedZ = False
#     dirIndex = 0
#     while (not reachedZ):
#         zSteps += 1
#         direction = dirs[dirIndex % len(dirs)]
#         dirIndex += 1

#         for index, so in enumerate(sources):
#             if (direction == 'L'):
#                 sources[index] = coords_map[so][0]
#             else:
#                 sources[index] = coords_map[so][1]
#         if all(s[-1] == 'Z' for s in sources):
#             break



#     return zSteps

# def process(file):
#     rows = [l.strip() for l in open(file).readlines()]
#     return rows

# def solve(file):
#     processed = process(file)
#     #print(f"Part 1: {solvePart1(processed)}")
#     print(f"Part 2: {solvePart2(processed)}")

# solve("inputs/08/input1.txt")


import re
import math

class Leaf:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __repr__(self) -> str:
        return f"({self.left}, {self.right})"

def part_1(instructions, tree):
    current_match = "AAA"
    total_iteration = 0
    iteration = 0
    while current_match != "ZZZ":
        if instructions[iteration] == "R":
            current_match = tree[current_match].right
        if instructions[iteration] == "L":
            current_match = tree[current_match].left

        total_iteration += 1
        iteration = (iteration + 1) % len(instructions)
        
    print(f"Part 1: {total_iteration}")

def part_2(instructions, tree):
    current_match_list = [key for key in tree.keys() if key.endswith('A')]

    total_iteration = 0
    iteration = 0
    while not all(isinstance(element, int) for element in current_match_list):
        for idx in range(len(current_match_list)):
            element = current_match_list[idx]
            if isinstance(element, int): continue
            if element.endswith('Z'):
                current_match_list[idx] = int(total_iteration)
                continue

            if instructions[iteration] == "R":
                element = tree[element].right
            if instructions[iteration] == "L":
                element = tree[element].left

            current_match_list[idx] = element

        total_iteration += 1
        iteration = (iteration + 1) % len(instructions)

    result = math.lcm(*current_match_list)
    print(f"Part 2: {result}")

with open("inputs/08/input1.txt") as data:
    lines = data.readlines()
    
    instructions = lines[0][0:-1]
    tree_lines = lines[2:]

    tree = {}
    pattern = re.compile(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)')
    for entry in tree_lines:
        match = pattern.match(entry)
        tree[match.group(1)] = Leaf(match.group(2), match.group(3))
    
    # Algorithm
    part_1(instructions, tree)
    part_2(instructions, tree)