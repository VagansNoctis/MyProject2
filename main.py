x = input().replace(' ', '')
value = ''
mas = []
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for ind, val in enumerate(x):
    if val in numbers:
        value += val
    else:
        if value != '':
            mas.append(int(value))
        mas.append(val)
        value = ''

mas.append(int(value))

if mas[0] != '-':
    mas.insert(0, '+')

print(mas)

sum = 0

for i in range(0, len(mas), 2):
    if mas[i] == '+':
        sum += mas[i + 1]
    else:
        sum -= mas[i + 1]

print(sum)
