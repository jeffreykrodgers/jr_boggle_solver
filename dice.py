import random

dice = [
    'AAAFRS', 'AAEEEE', 'AAFIRS', 'ADENNN', 'AEEEEM',
    'AEEGMU', 'AEGMNN', 'AFIRSY', 'BJKQXZ', 'CCNSTW',
    'CEIILT', 'CEILPT', 'CEIPST', 'DHHNOT', 'DHHLOR',
    'DHLNOR', 'DDLNOR', 'EIIITT', 'EMOTTT', 'ENSSSU',
    'FIPRSY', 'GORRVW', 'HIPRRY', 'NOOTUW', 'OOOTTU',
]

out = []

# each cell needs 1 die, so we need at least n*m total dice

n = 15
m = 15
area = n * m

for y in xrange(n):
    row = [0] * m
    for x in xrange(m):
        die = random.choice(dice)
        letter = random.choice(die)
        row[x] = letter
    out.append(''.join(row))
print '\n'.join(out)
