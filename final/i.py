def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
text = list(input().split(' '))
dct = {}
analysis(text, dct)
for key in sorted(dct.keys()) :
    print(key , dct[key])