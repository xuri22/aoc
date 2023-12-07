

with open("input/input_code4.txt") as file:
    sum = 0
    for line in file:
        winning = [int(x) for x in list(filter(lambda a: a != '', line.split(':')[1].split('|')[0].split(' ')))]
        own = [int(x) for x in list(filter(lambda a: a != '', line.split(':')[1].split('|')[1].split(' ')))]

        p = 0.5
        for num in own:
            if num in winning:
                p *= 2

        if p >= 1:
            sum += p

print(sum)
