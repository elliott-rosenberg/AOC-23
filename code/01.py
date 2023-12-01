import re


def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows


def solvePart1(file):
    calibration_sum = 0
    for row in file:
        num_row = re.findall(r'\d', row)
        calibration_sum += int(num_row[0] + num_row[-1])
    return calibration_sum




        
    
    

def solvePart2(file):
    calibration_sum = 0
    for row in file:
        matched_row = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', row)


        first_num = matched_row[0] if len(matched_row[0]) == 1 else word_to_num.get(matched_row[0])
        last_num = matched_row[-1] if len(matched_row[-1]) == 1 else word_to_num.get(matched_row[-1])
        # print(matched_row)
        # print(first_num)
        # print(last_num)
        # print( int(first_num + last_num))
        # print(calibration_sum)
        calibration_sum += int(first_num + last_num)


    return calibration_sum


word_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}



def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/01/input1.txt")