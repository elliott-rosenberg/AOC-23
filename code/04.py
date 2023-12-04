import re

def solvePart1(file):
    match_sum = 0
    for row in file:
        splitted = row.split('|')
        winning_nums = splitted[0].split(':')[1].strip().split(' ')
        for l in winning_nums:
            if l == '':
                winning_nums.remove(l)
        card_nums = splitted[1].strip().split(' ')
        for l in card_nums:
            if l == '':
                card_nums.remove(l)
        # print(winning_nums)
        # print(card_nums)

        matches = 0
        for num in winning_nums:
            for c_num in card_nums:
                if int(num) == int(c_num):
                    matches += 1
        if not matches == 0:
            match_sum += 2 ** (matches - 1)
                        

                        
    return match_sum

def solvePart2(file):
    card_total = 0
    card_copies = [1 for _ in range(len(file))]
    for row in file:
        
        splitted = row.split('|')
        winning_nums = splitted[0].split(':')[1].strip().split(' ')
        card_number = int(re.findall('\d+', splitted[0].split(':')[0])[0])
        print(card_number)
        card_multiplier = card_copies[card_number-1]
        for l in winning_nums:
            if l == '':
                winning_nums.remove(l)
        card_nums = splitted[1].strip().split(' ')
        for l in card_nums:
            if l == '':
                card_nums.remove(l)

        matches = 0
        for num in winning_nums:
            for c_num in card_nums:
                if int(num) == int(c_num):
                    matches += 1
        for card in range(card_number, card_number + matches):
            card_copies[card] += card_multiplier
        card_total += card_copies[card_number-1]


        
    return card_total

def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/04/input1.txt")
