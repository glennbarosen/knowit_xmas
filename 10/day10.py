import operator
results = [i.split(',') for i in open('results.txt').readlines()]
participants = {}
for i in results:
    for p in i:
        participants[p] = 0
for i in results:
    for p in i:
        participants[p] += len(i) - (i.index(p) + 1)
winner = max(participants.items(), key=operator.itemgetter(1))[0]
print('%s-%d' % (winner, participants[winner]))