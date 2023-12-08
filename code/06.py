import re
def solvePart1(file):
    waysToBeat = 1
    times = file[0].split(':')[1]
    times = [int(l) for l in re.findall('\d+', times)]
    distances = file[1].split(':')[1]
    distances = [int(l) for l in re.findall('\d+', distances)]
    print(times)
    print(distances)
    for i in range(len(times)):
        waysToBeat *= getRange(times[i], distances[i])
    return waysToBeat


def getRange(time, record):
    lowBound = 0
    highBound = 0
    for i in range(1, time):
        
        hypDist = i * (time - i)
        # print("from bottom up")
        # print(hypDist)
        if hypDist > record:
            lowBound = i
            break
    for i in range(time, 1, -1):
        
        hypDist = i * (time - i)
        # print("from topDown")
        # print(hypDist)
        if hypDist > record:
            highBound = i
            break
    dist = highBound - lowBound + 1
    print(f"range {dist}")
    return dist

def solvePart2(file):
    waysToBeat = 1
    times = file[0].split(':')[1]
    times = [int(''.join(re.findall(r'\d', times)))]
    distances = file[1].split(':')[1]
    distances = [int(''.join(re.findall(r'\d', distances)))]
    for i in range(len(times)):
        waysToBeat *= getRange(times[i], distances[i])
    return waysToBeat

def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/06/input1.txt")
