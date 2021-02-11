# https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3850#1
n = input().split()
for i in range(len(n)):
    if n[i]== '0':
       n.remove('0')
       n.append('0')
    print(n[i],end = ' ')   