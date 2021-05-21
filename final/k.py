import math
num = list()
a = list(set(input().split()))
for i in a:
    try:
        if math.log2(int(i)).is_integer():
            num.append(int(i))
    except ValueError:
        pass
num.sort()

print(*num, sep = " ")