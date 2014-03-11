# 13 February 2014
# http://www.cs.umd.edu/Outreach/hsContest13/questions/all.pdf
# Problem 2

def areAnagrams(xs, ys):
    # build character frequency counter for each string
    # then compare counters
    counter1 = {}
    counter2 = {}
    for ch in xs:
        if ch in counter1:
            counter1[ch] = counter1[ch] + 1
        else:
            counter1[ch] = 1
    for ch in ys:
        if ch in counter2:
            counter2[ch] = counter2[ch] + 1
        else:
            counter2[ch] = 1
    return counter1 == counter2


print areAnagrams('blather', 'reblath')
print areAnagrams('maryland', 'landam')
print areAnagrams('bizarre', 'brazier')