# 15 February 2014
# http://community.topcoder.com/stat?c=problem_statement&pm=2402

def solve(xs):
    dp = {0: [xs[0], 0]} # 2D table: index -> [0 if this is included, 1 if this is not]
    for i in xrange(1, len(xs)):
        dp[i] = [xs[i], 0]
        for j in xrange(0, i - 1):
            if i == len(xs) - 1 and j == 0:
                # prevent head and last from clashing
                continue
            dp[i][0] = max(dp[i][0], dp[j][0] + xs[i])
        for j in xrange(0, i):
            dp[i][1] = max(dp[i][1], dp[j][0])
    print dp
    all_sums = []
    for val in dp.values():
        all_sums += val
    r = max(all_sums)
    if r == dp[len(xs) - 1][0]:
        r -= xs[-1]
        r += max(xs[0], xs[-1])
    return r
    

print solve([10, 3, 2, 5, 7, 8])
# print solve([11, 15])
# print solve([7, 7, 7, 7, 7, 7, 7])
# print solve([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# print solve([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72])

        
        
                
            
    
    