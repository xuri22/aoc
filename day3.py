import re
from functools import reduce

with open('input/input_code3.txt') as f:
    contents = f.read()


with open('input/input_code3.txt') as f:
    num_lines = len(f.readlines())

line_len = len(contents.split('\n')[0])

symbols = ''.join(set(contents)).replace('\n', '').replace('.', '')
symbols = ''.join([i for i in symbols if not i.isdigit()])

# print(symbols)

# if we add padding we get rid of the use cases for numbers that are next to the margins

# add padding -> one line of just periods before and after the text
row = ''.join(['.'*line_len])

contents = row + '\n' + contents
contents += '\n' + row

# add vertical padding
contents = contents.replace('\n', '.\n.')
contents = '.' + contents + '.'
print(contents)
contents = contents.replace('\n', '')

sum = 0

line_len += 2
n = []
# for num in res:
for m in re.finditer(r'\d+', contents):
    ok = 0
    num = int(m.group())
    neighbours = ''
    neighbours += contents[m.start()-1]
    neighbours += contents[m.end()]
    neighbours += contents[m.start()-1-line_len:m.end()-line_len+1]
    neighbours += contents[m.start()-1+line_len:m.end()+line_len+1]

    for sym in symbols:
        if sym in neighbours:
            ok = 1
            break
    if ok == 1:
        print('{}: {}'.format(num, neighbours))
        sum += num
        n.append(len(neighbours))

print()
print(sum)


# part 2

# dict having index_of_*: [num1, num2]
sharing = {}

for m in re.finditer(r'\d+', contents):
    num = int(m.group())

    indices_to_check = [m.start() - 1, m.end()]
    indices_to_check.extend([x for x in range(m.start()-1-line_len, m.end()-line_len+1)])
    indices_to_check.extend([x for x in range(m.start()-1+line_len, m.end()+line_len+1)])

    for ix in indices_to_check:
        if contents[ix] == '*':
            if ix in sharing.keys():
                sharing[ix].append(num)
            else:
                sharing[ix] = [num]


sum = 0
for key in sharing.keys():
    if len(sharing[key]) > 1:
        print(sharing[key])

        sum += reduce(lambda x, y: x*y, sharing[key])

print(sum)
