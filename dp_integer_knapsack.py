# 28 February 2014
# http://www.lsi.upc.edu/~mjserna/docencia/algofib/P06/tr111.pdf

class Item(object):

    def __init__(self, weight, value):
        self.w = weight
        self.v = value

def solve(max_weight, *items):
    dp = {} # DP table to store max value from j objects with max weight i
    for i in xrange(0, max_weight + 1):
        for j in xrange(0, len(items) + 1):
            # Initialize
            dp[(i, j)] = 0
    for i in xrange(1, max_weight + 1):
        for j in xrange(1, len(items) + 1):
            item = items[j - 1] # Current item
            if i - item.w < 0:
                # Current item weight is greater than the current max weight i
                dp[(i, j)] = dp[(i, j -1)] # This item must be excluded
                continue
            # Is it better (more profitable) if this item is...
            dp[(i, j)] = max(dp[(i - item.w, j - 1)] + item.v, # ...included?
                             dp[(i, j - 1)])                   # ...excluded?
    return dp[(max_weight, len(items))]

print solve(11, Item(1, 1), Item(2, 6), Item(5, 18), Item(6, 22), Item(7, 28))
print solve(21, Item(1, 1), Item(2, 6), Item(5, 18), Item(6, 22), Item(7, 28))
print solve(100, Item(1, 1), Item(2, 6), Item(5, 18), Item(6, 22), Item(7, 28))
print solve(0, Item(1, 1), Item(2, 6), Item(5, 18), Item(6, 22), Item(7, 28))
print solve(1, Item(1, 1), Item(2, 6), Item(5, 18), Item(6, 22), Item(7, 28))
