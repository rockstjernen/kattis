import sys
lines = int(sys.stdin.readline().strip())
i=0
for l in range(lines):
    i += 1
    line = str(sys.stdin.readline().strip())
    if i%2 == 1:
        print(line)

