import re

def solvePart1(file):


    id_sum = 0
    for row in file:
        row_id = int(re.split('[ :+]', row)[1])

        draws = re.split('[,;]+', row.split(':')[1])
        draws = [l.strip() for l in draws]
        id_good = True
        for draw in draws:
            num = int(draw.split(' ')[0]);
            letter = draw.split(' ')[1][0]
            if letter == 'b':
                if num > 14:
                    id_good = False
            if letter == 'r':
                if num > 12:
                    id_good = False
            if letter == 'g':
                if num > 13:
                    id_good = False
        if id_good:
            id_sum += int(row_id)
    return id_sum


def solvePart2(file):
    power_sum = 0
    for row in file:
        row_id = int(re.split('[ :+]', row)[1])

        draws = re.split('[,;]+', row.split(':')[1])
        draws = [l.strip() for l in draws]
        blue_total = 0
        red_total = 0
        green_total = 0
        for draw in draws:
            num = int(draw.split(' ')[0]);
            letter = draw.split(' ')[1][0]
            if letter == 'b':
                if num > blue_total:
                    blue_total = num
            if letter == 'r':
                if num > red_total:
                    red_total = num
            if letter == 'g':
                if num > green_total:
                    green_total = num

        power = blue_total * red_total * green_total
        power_sum += power
    return power_sum

def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/02/input1.txt")
