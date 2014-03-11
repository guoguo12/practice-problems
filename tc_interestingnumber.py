# 6 March 2014
# http://community.topcoder.com/stat?c=problem_statement&pm=13038

def interesting(n):
    n = str(n)
    for i in xrange(0, len(n) - 1):
        char = n[i]
        pos = n.find(char, i + 1) # find first occurrence of digit
        if pos != -1:
            if pos - i - 1 != int(char):
                # does not obey digit rule
                return False
            if n.find(char, pos + 1) != -1:
                # more than two occurrences of digit
                return False
    return True


print interesting(2002)
print interesting(1001)
print interesting(41312432)
print interesting(611)
print interesting(64200246)
print interesting(631413164)
print interesting(631413)
print interesting(6314103)
print interesting(6314)
print interesting(63143)
print interesting(6314333)
print interesting(63003)
print interesting(6300)
print interesting(0)