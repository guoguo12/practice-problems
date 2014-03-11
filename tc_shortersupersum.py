# 15 February 2014
# http://community.topcoder.com/stat?c=problem_statement&pm=10240

def supersum(k, n):
    dp = [[]]
    for x in xrange(0, n + 1):
        dp[0].append(x)
    for i in xrange(1, k + 1):
        dp.append([])
        for j in xrange(0, n + 1):
            dp[i].append(sum(dp[i - 1][:j + 1]))
    return dp[k][n]


print supersum(1, 3)
print supersum(2, 3)
print supersum(4, 10)
print supersum(10, 10)