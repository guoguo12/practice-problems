# 12 February 2014
# http://www.cs.berkeley.edu/~vazirani/algorithms/chap6.pdf

def solve(xs):
    dp = {}
    dp[0] = [xs[0]]
    # notice how using indices here is better than using enumerate()
    for i in xrange(1, len(xs)):
        x = xs[i]
        for j in xrange(0, i):
            y = xs[j]
            if x > y:
                if i in dp:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [x]
                else:
                    dp[i] = dp[j] + [x]
        if not i in dp:
            dp[i] = [x] # this is head of new increasing subarray
    longest = []
    for sub in dp.values():
        if len(sub) > len(longest):
            longest = sub
    return longest
    

xs = [5, 2, 8, 6, 3, 6, 9, 7]
print solve(xs)