prc = int(input('Введите число % от 1 до 20: '))

if prc == 1:
    print(prc, 'процент')
elif prc in range(2,5):
    print(prc, 'процента')
else:
    print(prc, 'процентов')