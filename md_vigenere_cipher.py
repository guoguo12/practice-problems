# 14 February 2014
# http://www.cs.umd.edu/Outreach/hsContest12/questions/all.pdf
# Problem 3

# assumes ch is uppercase
def rot(ch, offset):
    return chr((ord(ch) - 65 + offset) % 26 + 65)

def vigenere(keyword, plaintxt):
    result = ''
    keywordIndex = 0
    for ch in plaintxt:
        offset = ord(keyword[keywordIndex]) - 65
        result += rot(ch, offset)
        keywordIndex += 1
        keywordIndex %= len(keyword)
    return result


print vigenere('LEMON', 'ATTACKATDAWN')
print vigenere('ABCD', 'CRYPTOISSHORTFORCRYPTOGRAPHY')
print vigenere('ABCDE', 'CRYPTOISSHORTFORCRYPTOGRAPHY')
print vigenere('LUCKY', 'COMPUTINGGIVESINSIGHT')