text = list(input().split())
answer = " "
dct = {}
def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1

analysis(text,dct)
max_key = max(dct, key=dct.get)
print(max_key.upper())
