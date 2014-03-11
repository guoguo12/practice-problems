# 15 February 2014
# http://community.topcoder.com/stat?c=problem_statement&pm=1259

def solve(xs):
    dp = {0: [1, 1]} # 2D table: index -> [0 for up next | 1 for down next]
    for i in xrange(1, len(xs)):
        dp[i] = [1, 1]
        for j in xrange(0, i):
            if xs[i] > xs[j]:
                opt_so_far = dp[j][0] # going up this time
                dp[i][1] = max(dp[i][1], opt_so_far + 1) # going down next
            elif xs[i] < xs[j]:
                opt_so_far = dp[j][1] # going down this time
                dp[i][0] = max(dp[i][0], opt_so_far + 1) # going up next
            else:
                continue
    all_lengths = []
    for val in dp.values():
        all_lengths += val
    return max(all_lengths)


print solve([1, 7, 4, 9, 2, 5])
print solve([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
print solve([44])
print solve([1, 2, 3, 4, 5, 6, 7, 8, 9])
print solve([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32])
print solve([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244])