# https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3835#1
n = input().split()
m = 1000
for i in range(len(n)):
    b = int(n[i])
    if (b < m) and (b > 0):
         m = b
print(m)            