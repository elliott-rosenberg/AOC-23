import re


def solvePart1(file):
    winnings = 0
    hand_map = {}
    for row in file:
        hand = row.split(" ")[0]
        bet = int(row.split(" ")[1])
        hand_map[hand] = bet

    print(hand_map)
    rankings = []
    firstHand = True
    for hand in hand_map.keys():
        if firstHand:
            rankings.append(hand)
            firstHand = False
        else:
            i = 0
            lastHand = False
            while(compareHands(hand, rankings[i])):
                i+=1
                if i == len(rankings):
                    lastHand = True
                    break
            rankings.insert(i, hand)
    # print(rankings)

    for a, holding in enumerate(reversed(rankings)):
        # print(f"rank: {a} holding: {holding}")
        winnings += hand_map[holding] * (a + 1)


    return winnings



ranking_map = {}
def compareHands(hand1, hand2):
    if hand2 in ranking_map:
        strength2 = ranking_map.get(hand2)
    else:
        strength2 = getStrengthVal(hand2)
    strength1 = getStrengthVal(hand1)
    if strength2 > strength1:
        return True
    elif strength2 == strength1:
        for i in range(5):
            if strength_rankings[hand1[i]] == strength_rankings[hand2[i]]:
                continue
            else:
                return strength_rankings[hand2[i]] > strength_rankings[hand1[i]]
        print("shouldn't be here")
    else:
        return False


def getStrengthVal(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    rank_vals = sorted(char_count.values(), reverse=True)
    match rank_vals[0]:
        case 5:
            currStrength = 6
        case 4:
            currStrength = 5
        case 3:
            if rank_vals[1] == 2:
                currStrength = 4
            else:
                currStrength = 3
        case 2:
            currStrength = 1
        
            if rank_vals.count(2) > 1:
                currStrength = 2
        case 1:
            currStrength = 0
        case _:
            print("bad news")
            print(hand)
    ranking_map[hand] = currStrength
    return currStrength


strength_rankings = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
    }

def solvePart2(file):
    winnings = 0
    hand_map = {}
    for row in file:
        hand = row.split(" ")[0]
        bet = int(row.split(" ")[1])
        hand_map[hand] = bet
    rankings = []
    firstHand = True
    for hand in hand_map.keys():
        if firstHand:
            rankings.append(hand)
            firstHand = False
        else:
            i = 0
            lastHand = False
            while(compareHands2(hand, rankings[i])):
                i+=1
                if i == len(rankings):
                    lastHand = True
                    break
            rankings.insert(i, hand)
    # print(rankings)

    for a, holding in enumerate(reversed(rankings)):
        # print(f"rank: {a} holding: {holding}")
        winnings += hand_map[holding] * (a + 1)


    return winnings



ranking_map2 = {}
def compareHands2(hand1, hand2):
    if hand2 in ranking_map2:
        strength2 = ranking_map2.get(hand2)
    else:
        strength2 = getStrengthVal2(hand2)
    if hand1 in ranking_map2:
        strength1 = ranking_map2.get(hand1)
    else:
        strength1 = getStrengthVal2(hand1)
    if strength2 > strength1:
        return True
    elif strength2 == strength1:
        for i in range(5):
            if strength_rankings2[hand1[i]] == strength_rankings2[hand2[i]]:
                continue
            else:
                return strength_rankings2[hand2[i]] > strength_rankings2[hand1[i]]
        print("shouldn't be here")
    else:
        return False


def getStrengthVal2(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    if 'J' in char_count:
        if char_count['J'] != 5:
            j_value = char_count.pop('J')
            highest_value_key = max(char_count, key=char_count.get)
            char_count[highest_value_key] += j_value

    rank_vals = sorted(char_count.values(), reverse=True)
    match rank_vals[0]:
        case 5:
            currStrength = 6
        case 4:
            currStrength = 5
        case 3:
            if rank_vals[1] == 2:
                currStrength = 4
            else:
                currStrength = 3
        case 2:
            currStrength = 1
        
            if rank_vals.count(2) > 1:
                currStrength = 2
        case 1:
            currStrength = 0
        case _:
            print("bad news")
            print(hand)
    ranking_map2[hand] = currStrength
    return currStrength


strength_rankings2 = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 0,
    'Q': 10,
    'K': 11,
    'A': 12
    }


def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {solvePart1(processed)}")
    print(f"Part 2: {solvePart2(processed)}")

solve("inputs/07/input1.txt")
