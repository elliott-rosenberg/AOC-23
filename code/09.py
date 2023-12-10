def solvePart1(file):
    history_sum = 0
    values = []
    for row in file:
        values.append([int(l) for l in row.split(' ')])
    for v in values:
        # print(f"value: {v}")
        history_sum += getDif([v[-1]], v)
    return history_sum



def getDif(lastVals, inList) -> int:
    nextList = []
    for i in range(len(inList)-1):
        nextList.append(inList[i+1] - inList[i])
    lastVals.append(nextList[-1])
    if len(set(nextList)) == 1:
        # print(f"next input: {nextList}")
        # print(f"lastVals: {lastVals}")
        return sum(lastVals)
    else:
        return getDif(lastVals, nextList)

def getSecondDif(lastVals, inList) -> int:
    nextList = []
    for i in range(len(inList)-1):
        nextList.append(inList[i+1] - inList[i])
    lastVals.append(nextList[0])
    #print(f"next input: {nextList}")
    if all(ele == 0 for ele in nextList):
        out = 0
        for i in range(len(lastVals), 0, -1):
            out = lastVals[i-1] - out
        #print(f"lastVals: {lastVals}")
        return out
    else:
        return getSecondDif(lastVals, nextList)






def solvePart2(file):
    history_sum = 0
    values = []
    for row in file:
        values.append([int(l) for l in row.split(' ')])
    for v in values:
        #print(f"value: {v}")
        history_sum += getSecondDif([v[0]], v)
    return history_sum

def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")



solve("inputs/09/input1.txt")
