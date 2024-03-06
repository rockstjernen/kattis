import sys

parties, seats = sys.stdin.readline().split()
parties, seats = int(parties), int(seats)

pvotes = [0] * parties
pseats = [0] * parties


for p in range(parties):
    pvotes[p] = (int(sys.stdin.readline()))

    #print(pvotes[p])

for _ in range(seats):
    best = 0
    for p in range(1,parties):
        if pvotes[p] / (1 + pseats[p]) > pvotes[best] / (1 + pseats[best]):
            best = p
    pseats[best] += 1
    
for seat in pseats:
    print(seat)