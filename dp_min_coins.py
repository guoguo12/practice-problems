# 12 February 2014
# http://people.cs.clemson.edu/~bcdean/dp_practice/

# precondition: 1 is an element of denoms
def min_coins(denoms, amount):
    dp = {} # DP table
    dp[0] = 0 # zero coins for amount = 0
    for x in xrange(1, amount + 1):
        for dn in denoms:
            if x - dn >= 0:
                if x in dp:
                    dp[x] = min(dp[x - dn] + 1, dp[x])
                else:
                    dp[x] = dp[x - dn] + 1
    return dp[amount]
            

denoms = [1, 5, 10, 25]
amount = 21
print min_coins(denoms, amount)