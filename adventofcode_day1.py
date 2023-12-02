def read_file(filename):
    result1 = 0
    result2 = 0
    with open(filename) as datafile:
        for line in datafile:
            result1 += get_digits_part_1(line)
            result2 += get_digits_part_2(line)
    return result1, result2

def get_digits_part_1(string):
    num = ''
    for i in range(len(string)):
        if string[i].isdigit():
            num += string[i]
            break

    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            num += string[i]
            break
    return int(num)

def get_digits_part_2(string):
    for key, value in num_dic.items():
        string = string.replace(key, value)
    return get_digits_part_1(string)

num_dic = { 'one': 'o1e',
            'two': 't2o',
            'three': 't3e',
            'four': 'f4r',
            'five': 'f5e',
            'six': 's6x',
            'seven': 's7n',
            'eight': 'e8t',
            'nine': 'n9e'}

part1, part2 = read_file('input.txt')
print(f'{part1=}')
print(f'{part2=}')