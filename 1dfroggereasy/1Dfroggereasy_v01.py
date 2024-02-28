import sys
pads, start, magic = sys.stdin.readline().split()
pads, start, magic = int(pads), int(start), int(magic)
map = sys.stdin.readline().split()
visited = set()

jumps = 0
location = start

while True:
    if location < 1:
        print('left')
        print(jumps)
        break
    elif location > pads:
        print('right')
        print(jumps)
        break
    elif location in visited:
        print('cycle')
        print(jumps)
        break
    elif int(map[location-1]) == magic:
        print('magic')
        print(jumps)
        break
    
    #print(jumps, visited, location, map[location-1])

    jumps += 1
    visited.add(location)

    location += int(map[location-1])

    #value = int(map[location])
    
    #print(jumps, visited)
