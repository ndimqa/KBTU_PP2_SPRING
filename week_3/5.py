# https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3853#1
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

n = input().split()
k = int(input())
shift(n,k)
print(n)