
def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows


def solvePart1(file):
    calibration_sum = 0
    for row in file:
        calibration_value=0


        
    
    

# def solvePart2(file):





def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    #print(f"Part 2: {solvePart2(processed)}")

solve("inputs/01/input1.txt")