# 14 February 2014
# http://www.cs.umd.edu/Outreach/hsContest10/questions/all.pdf
# Problem 2

def solve(input):
    rows = []
    cols = []
    chunks = input.split()
    count = int(chunks[0])
    for i in xrange(0, count):
        rows.append(chunks[2 * i + 1])
        cols.append(chunks[2 * i + 2])
    if elementsUnique(rows) and elementsUnique(cols):
        return 'SAFE'
    else:
        return 'NOT SAFE'

def elementsUnique(xs):
    xs = sorted(xs)
    for i in xrange(1, len(xs)):
        if xs[i] == xs[i - 1]:
            return False
    return True


print solve('3 1 1 2 6 8 8')
print solve('2 2 3 1 3')