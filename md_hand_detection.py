# 13 February 2014
# http://www.cs.umd.edu/Outreach/hsContest13/questions/all.pdf
# Problem 1

def detectSpread(cards):
    diffs = []
    for i in xrange(0, len(cards) - 1):
        for j in xrange(i + 1, len(cards)):
            diffs.append(abs(cards[i][1] - cards[j][1]))
    diffs = sorted(diffs)
    for i in xrange(0, len(diffs) - 1):
        if diffs[i] == diffs[i + 1]:
            return False
    return True

def detectRainbow(cards):
    for x in xrange(0, 5):
        suitExists = False
        for card in cards:
            if card[0] == x:
                suitExists = True
                break
        if not suitExists:
            return False
    return True


# card format: (suit, value)
t1 = [(0, 1), (0, 2), (0, 4), (0, 8), (0, 16)]
t2 = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]

print detectSpread(t1)
print detectSpread(t2)
print detectRainbow(t1)
print detectRainbow(t2)
