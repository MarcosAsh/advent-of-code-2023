from collections import defaultdict

FILE = "input"

# seeds:dict[int, int] = {} # part 1
seeds:list[int] = [] # part 1
seed_ranges:list[tuple[int, int]] = [] # part 2

# dict<(element 1, element 2): list[(dest, source, len)]>
element_map:dict[tuple[int, int], list[tuple[int, int, int]]] = defaultdict(list)
ele_index = -1

with open(FILE) as f:
    for i, line in enumerate(f.read().splitlines()):
        if i == 0:
            nums_list = line.lstrip("seeds: ").split(" ")
            seeds = [int(n) for n in nums_list]
            for i in range(len(nums_list)//2):
                seed_ranges.append( (int(nums_list[i*2]), int(nums_list[i*2+1])) )
            continue
        if not line:
            ele_index += 1
            continue
        if line.endswith("map:"):
            continue
        dest, source, length = map(int, line.split(" "))
        element_map[(ele_index, ele_index+1)].append((dest, source, length))

for i in range(ele_index+1):
    # part 1
    for j, loc in enumerate(seeds):
        for destg, sourceg, leng in element_map[(i, i+1)]:
            if sourceg <= loc < sourceg+leng:
                seeds[j] = destg - sourceg + loc
                break
    # part 2
    checked = set()
    for destg, sourceg, leng in element_map[(i, i+1)]:
        diff = destg - sourceg
        for j in range(len(seed_ranges)):
            if j in checked: continue
            start, len_s = seed_ranges[j]
            if start >= sourceg and start+len_s <= sourceg+leng:
                checked.add(j)
                seed_ranges[j] = (diff+start, len_s)
            elif start < sourceg and start+len_s <= sourceg+leng and start+len_s >= sourceg:
                checked.add(j)
                seed_ranges[j] = (diff+sourceg, len_s+start-sourceg)
                seed_ranges.append( (start, sourceg-start) )
            elif start >= sourceg and start+len_s > sourceg+leng and start <= sourceg+leng:
                checked.add(j)
                seed_ranges[j] = (diff+start, -start+sourceg+leng)
                seed_ranges.append( (sourceg+leng, start+len_s-sourceg-leng) )
            elif start < sourceg and start+len_s > sourceg+leng:
                checked.add(j)
                seed_ranges[j] = (diff+sourceg, -start-start+leng)
                seed_ranges.append( (sourceg+leng, start+len_s-sourceg-leng) )
                seed_ranges.append( (start, start-sourceg) )
            if len(checked) == len(seed_ranges): break
        # print(seed_ranges)
        if len(checked) == len(seed_ranges): break
    # print("\n\n")

min_location1 = min(seeds)
min_location2 = min(seed_ranges, key=lambda v:v[0])

# print(seed_ranges)
# for k, v in element_map.items():
#     print(k, v)

print("Part 1:", min_location1)
print("Part 2:", min_location2[0])