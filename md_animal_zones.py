# 27 February 2014
# http://www.cs.umd.edu/Outreach/hsContest06/questions/all.pdf
# Problem 1

def solve(*rects):
    s = {}
    for rect in rects:
        for x in xrange(rect[0], rect[2] + 1):
            for y in xrange(rect[1], rect[3] + 1):
                if (x, y) in s:
                    return "Overlap"
                else:
                    s[(x, y)] = '1'
    return "No Overlap"


print solve([1, 1, 2, 2], [2, 5, 4, 7], [4, 2, 7, 3])
print solve([1, 1, 2, 2], [2, 2, 5, 3])
print solve([2, 2, 4, 4], [3, 1, 5, 3], [3, 1, 6, 6], [7, 1, 8, 8])
print solve([0, 0, 5, 0], [0, 2, 5, 2], [0, 3, 5, 3], [0, 5, 5, 5])