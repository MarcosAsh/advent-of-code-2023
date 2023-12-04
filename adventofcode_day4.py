# Part 1
card_map = {}
for l in open("input day 4").readlines():
    card_str, numbers_str = l.split(": ")
    ls, rs = numbers_str.split(" | ")
    card_map[int(card_str.split()[1])] = len(set(ls.split()) & set(rs.split()))

print("1:", sum(pow(2, matches-1) for matches in card_map.values() if matches))

# Part 2
copies = { c: 1 for c in card_map }
for c in card_map:
    for x in range(card_map[c]):
        copies[c + 1 + x] += copies[c]

print("2:", sum(copies.values()))