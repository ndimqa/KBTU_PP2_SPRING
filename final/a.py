#a
import math
number = list(input().split())
numbers = list()
for i in range(int(number[0]),int(number[1])):
    try:
        if math.log(i,3).is_integer() and i >= 1000 and i<=9999:
               numbers.append(int(i)) 
    except ZeroDivisionError:
        pass
numbers.sort(reverse=True)     
print(*numbers, sep = " ")
