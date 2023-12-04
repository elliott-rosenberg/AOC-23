import re

def solvePart1(file):
    parts_sum = 0
    engine_array = []
    amt = len(file[0]) + 2
    first = ['.' for _ in range(amt)]
    engine_array.append(first)
    for row in file:
        engine_row = []
        engine_row.append('.')
        [engine_row.append(l) for l in row]
        engine_row.append('.')
        engine_array.append(engine_row)
    engine_array.append(first)
    for rowIndex, row in enumerate(engine_array):
        # print(row)
        numStart = False
        num = ''
        for colIndex, entry in enumerate(row):
            if entry.isdigit():
                numStart = True
                num = num + entry
            if (not entry.isdigit()) and numStart:
                numStart = False
                isPart = checkPart(engine_array, rowIndex, colIndex, len(num))
                if isPart:
                    parts_sum += int(num)
                num = ''
                #if at this point we can check for symbols in the previous spots
    return parts_sum
        

        


def checkPart(engArray, row, col, numLen) -> bool:
    for rowInd in range(row-1, row+2):
        for colInd in range(col - numLen - 1, col + 1):
            if len(re.findall('[^.\d]', engArray[rowInd][colInd])) > 0:
                return True
    return False

def solvePart2(file):
    ratio_sum = 0
    engine_array = []
    amt = len(file[0]) + 2
    first = ['.' for _ in range(amt)]
    engine_array.append(first)
    for row in file:
        engine_row = []
        engine_row.append('.')
        [engine_row.append(l) for l in row]
        engine_row.append('.')
        engine_array.append(engine_row)
    engine_array.append(first)
    for rowIndex, row in enumerate(engine_array):
        # print(row)
        numStart = False
        num = ''
        for colIndex, entry in enumerate(row):
            if entry.isdigit():
                numStart = True
                num = num + entry
            if (not entry.isdigit()) and numStart:
                numStart = False
                isPart = checkRatio(engine_array, rowIndex, colIndex, len(num), int(num))
                num = ''
                #if at this point we can check for symbols in the previous spots
    print(num_map)
    for val in num_map.values():
        if len(val) == 2:
            ratio_sum += val[0] * val[1]
    return ratio_sum

num_map = {}

def checkRatio(engArray, row, col, numLen, num) -> bool:
    for rowInd in range(row-1, row+2):
        for colInd in range(col - numLen - 1, col + 1):
            if engArray[rowInd][colInd] == '*':
                print(num)
                key = f"{rowInd} {colInd}"
                if not key in num_map:
                    num_map[key] = [num]
                else:
                    val = num_map[key]
                    val.append(num)
                    num_map[key] = val

            if len(re.findall('[^.\d]', engArray[rowInd][colInd])) > 0:
                return True
    return False


def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/03/input1.txt")
