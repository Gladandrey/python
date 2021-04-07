number = [i**3 for i in range(1,1001,2)]
print(number)
print()

def sum_digits(value):
    res = 0
    while value != 0:
        res += value % 10
        value //= 10
    return res
res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, number))
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, number))
print(res1)
print(res2)
print()

print(sum(filter(lambda j: sum(map(int, str(j))) % 7 == 0, number)))
print(sum(filter(lambda j: sum(map(int, str(j + 17))) % 7 == 0, number)))
