import sys
lines = int(sys.stdin.readline())
data = []
qaly = 0.0
for l in range(lines):
    line = sys.stdin.readline().split()
    data.append([float(line[0]), float(line[1])])

for i in data:
    qaly += i[0] * i[]

print(qaly)