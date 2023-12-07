import re

filename = "input/input_code1.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

# part 1
sum = 0
for code in lines:
    temp = re.findall(r'\d', code)
    res = list(map(int, temp))
    number = res[0]*10 + res[-1]
    sum += number

print(sum)

# part 2

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits_dict = {}

for i, d in enumerate(digits):
    digits_dict[d] = i

digits = digits[1:]

sum = 0
print()
for code in lines:
    for d in digits:
        if d in code:
            code = code.replace(d, d[0] + str(digits_dict[d]) + d[-1])

    temp = re.findall(r'\d', code)
    res = list(map(int, temp))
    number = res[0] * 10 + res[-1]
    sum += number

print()
print(sum)


