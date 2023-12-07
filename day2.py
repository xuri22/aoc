import re

filename = "input/input_code2.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

max_red = 12
max_green = 13
max_blue = 14

games = {}

# part 1

sum = 0
for game in lines:
    ok = 1
    temp = re.findall(r'\d+', game)
    res = list(map(int, temp))
    id = res[0]
    res = res[1:]
    if max(res) > 14:
        ok = 0
        continue
    else:
        if max(res) == 14:
            for m in re.finditer('14', game):
                if game[m.end() + 1] in ['r', 'g']:
                    ok = 0
                    break

            if '13' in game:
                for m in re.finditer('13', game):
                    if game[m.end() + 1] == 'r':
                        ok = 0
                        break

        if max(res) == 13:
            for m in re.finditer('13', game):
                if game[m.end() + 1] == 'r':
                    ok = 0
                    break
    if ok == 1:
        sum += id


print(sum)

# part 2

colours = ['red', 'green', 'blue']
sum = 0
for game in lines:
    l = []
    d = {}
    for i, col in enumerate(colours):
        aux = []
        for m in re.finditer(col, game):
            # just one digit
            if game[m.start() - 3] == ' ':
                num = int(game[m.start() - 2])
            else:
                num = int(game[m.start() - 3] + game[m.start() - 2])

            aux.append(num)

        d[col] = max(aux)
    p = 1
    for key in d.keys():
        p *= d[key]

    print(p)
    sum += p

print(sum)





