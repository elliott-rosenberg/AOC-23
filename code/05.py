# import re
# def solvePart1(file):
#     firstLine = True
#     incomingMap = False
#     seeds = []
#     maps = []
#     for row in file:
#         if firstLine:
#             firstLine = False
#             seeds = row.split(':')[1].strip().split(' ')
#             seeds = [int(seed) for seed in seeds]
#         if row == '':
#             incomingMap = False
#         if incomingMap:
#             nums = re.findall('\d+', row)
#             nums = [int(num) for num in nums]
#             maps[-1].append(nums)
#         if len(re.findall('map', row)) > 0:
#             incomingMap = True
#             maps.append([])
#             continue
#     return getSmallestLocation(seeds, maps)

# def getSmallestLocation(seeds, maps):
#     smallestLocation = float("inf")
#     newInput = seeds
#     for sMap in maps:
#         for index, seed in enumerate(newInput):
#             accessed = False
#             for pairing in sMap:
#                 if (seed >= pairing[1]) and (seed < pairing[1] + pairing[2]):
#                     accessed = True
#                     # print(f"seed{seed} dest: {pairing[0] } source: {pairing[1]} range {pairing[2]}")
#                     # print(f" new value:{seed - (pairing[1] - pairing[0])}")
#                     newInput[index] = (seed - (pairing[1] - pairing[0]))
#                     break
#             if not accessed:
#                 newInput[index] = seed   
#     return min(newInput)
    
                




# def solvePart2(file):
#     firstLine = True
#     incomingMap = False
#     seeds = []
#     maps = []
#     for row in file:
#         if firstLine:
#             firstLine = False
#             unparsedSeeds = row.split(':')[1].strip().split(' ')
#             unparsedSeeds = [int(seed) for seed in unparsedSeeds]
#             seeds = []
#             for x in range(len(unparsedSeeds) - 1):
#                 if x % 2 == 0:
#                     for i in range(unparsedSeeds[x+1]):
#                         seeds.append(unparsedSeeds[x] + i)
        
#         if row == '':
#             incomingMap = False
#         if incomingMap:
#             nums = re.findall('\d+', row)
#             nums = [int(num) for num in nums]
#             maps[-1].append(nums)
#         if len(re.findall('map', row)) > 0:
#             incomingMap = True
#             maps.append([])
#             continue
#     return getSmallestLocation(seeds, maps)


# def process(file):
#     rows = [l.strip() for l in open(file).readlines()]
#     return rows

# def solve(file):
#     processed = process(file)
#     print(f"Part 1: {solvePart1(processed)}")
#     print(f"Part 2: {solvePart2(processed)}")

# solve("inputs/05/input1.txt")


def map_section(bounds, next_map):
    next_ranges = []
    bounds = [bounds]
    for m in next_map:
        for i, bound in enumerate(bounds):
            #If bounds completely encapsulated
            if bound[0] >= m[0][0] and bound[1] <= m[0][1]:
                next_ranges.append([(bound[0] - m[0][0]) +  m[1][0], (bound[1] - m[0][0]) + m[1][0]])
                bound[0] = bound[1]
                break
            elif bound[0] < m[0][0] and bound[1] > m[0][1]:
                next_ranges.append([0 + m[1][0], (m[0][1] - m[0][0]) + m[1][0]])
                del bounds[i]
                bounds.extend([[bound[0], m[0][0]], [m[0][1], bound[1]]])
            #If not complete encapsulation
            if bound[0] >= m[0][0] and bound[0] < m[0][1]:
                next_ranges.append([(bound[0] - m[0][0]) +  m[1][0], (m[0][1] - m[0][0]) +  m[1][0]])
                bound[0] = m[0][1]
            elif bound[1] >= m[0][0] and bound[1] <= m[0][1]:
                next_ranges.append([0 +  m[1][0], (bound[1] - m[0][0]) +  m[1][0]])
                bound[1] = m[0][0]
    #No bound overlap
    for bound in bounds:
        if bound[0] != bound[1]:
            next_ranges.append([bound[0], bound[1]])
    return next_ranges

with open('inputs/05/input1.txt') as f:
    maps = f.read().split('\n\n')
    seeds, maps = maps[0].split()[1:], maps[1:]
    for i, m in enumerate(maps):
        maps[i] = m.split('\n')[1:]
        maps[i] = [[[s, s + r], [d, d + r]] 
                        for d, s, r in [map(int, x.split()) for x in maps[i]]]

part_one, part_two = [], []
for i in range(len(seeds)):
    part_one.append([int(seeds[i]), int(seeds[i]) + 1])
    if i % 2 == 0:
        part_two.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])])
for m in maps:
    part_one = sum(list(map(map_section, part_one, [m]*len(part_one))), [])
    part_two = sum(list(map(map_section, part_two, [m]*len(part_two))), [])

#Results
print(min([x[0] for x in part_one])) #Part 1
print(min([x[0] for x in part_two])) #Part 2