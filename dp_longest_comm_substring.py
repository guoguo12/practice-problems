# 28 February 2014
# https://en.wikipedia.org/wiki/Longest_common_substring_problem

def longest(s1, s2):
    dp = {} # DP table mapping (i, j) to longest subsequence ending here
    z = 0 # Stores length of current best(s)
    ret = [] # Stores current best(s)
    for i in xrange(0, len(s1)):
        for j in xrange(0, len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    # Starting at beginning
                    dp[(i, j)] = 1
                else:
                    # Continuing existing match
                    dp[(i, j)] = dp[i - 1, j - 1] + 1
                if dp[(i, j)] > z:
                    # Current match is best
                    z = dp[(i, j)]
                    ret = [s1[i - z + 1 : i + 1]]
                elif dp[(i, j)] == z:
                    # Current match is as good as best
                    ret.append(s1[i - z + 1 : i + 1])
            else:
                # Could also occur at beginning when initializing dp
                dp[(i, j)] = 0
    return ret


print longest('abcdef', 'fedabc')
print longest('3.141592653589793238462643', '3832795028841971693993751058209')
print longest('1234asdfasdfasdfasdf1234', '3467asdfasdfasdfasdf3467')
print longest('algorithm', 'implementation')
print longest('', '')
