# 13 February 2014
# http://www.cs.umd.edu/Outreach/hsContest13/questions/all.pdf
# Problem 3

def solve(secret, guess):
    # cast
    s = str(secret)
    g = str(guess)
    # pad
    while len(s) < 4:
        s = '0' + s
    while len(g) < 4:
        g = '0' + g
    # save copy to display
    sc = s
    gc = g
    # find circles and squares
    circles = 0
    squares = 0
    for i in xrange(0, 4):
        for j in xrange(0, 4):
            if g[i] == s[j]:
                if i == j:
                    circles += 1
                else:
                    squares += 1
                s = s[:j] + 'x' + s[j + 1:] # no more matches allowed for this secret character
                break # no more matches allowed for this guess character
    print 'For secret = %s and guess = %s, %d circles and %d squares will light up.' % (sc, gc, circles, squares)


# from problem description
solve(1234, 1357)
solve(1234, 1122)
solve(1311, 1122)
solve(11, 213)
# from examples
solve(1234, 1111)
solve(5678, 5678)
solve(4444, 4444)
solve(1234, 1211)
solve(1122, 2211)