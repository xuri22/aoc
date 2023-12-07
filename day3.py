import re

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


temp = re.findall(r'\d+', contents)
res = list(set(map(int, temp)))

sum = 0

line_len += 2
n = []
# for num in res:
for m in re.finditer(r'\d+', contents):
    ok = 0
    num = int(m.group())
    digits = len(str(num))
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



