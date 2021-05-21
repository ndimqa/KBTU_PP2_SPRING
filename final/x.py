n = int(input())
d = {}
all_p = 0
for i in range(0,n):
    word = input().split()
    key = word[0]
    value = int(word[1])
    if key in d:
        d[key] += value
    else:
        d[key] = value
    all_p = all_p + int(value)

for i in d:
    num = (int(d[i])/all_p)*100
    if num.is_integer:
        d[i] = f'{num:.5f}'[:-1]
    else:
        d[i]=num
    
sorted_dict = dict( sorted(d.items(),
                           key=lambda item: item[1],
                           reverse=True))
for key in sorted_dict.keys() :
    print(key , sorted_dict[key],"%")