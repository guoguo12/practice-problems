# 12 February 2014
# http://people.cs.clemson.edu/~bcdean/dp_practice/

def solve(xs):
    max_sum = optimal_so_far = xs[0]
    for x in xs[1:]:
        # compute max of subarray ending here
        # either this is part of an existing subsequence
        # or the start of a new one
        optimal_so_far = max(optimal_so_far + x, x) # compute subproblem using prior subproblems
        max_sum = max(max_sum, optimal_so_far)      # update solution
    return max_sum
        
xs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print solve(xs)
    