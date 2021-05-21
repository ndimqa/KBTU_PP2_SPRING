n = input()
m = input()
n.lower()
m.lower()

if(sorted(m)==sorted(n)):
    print("YES")
else:
    print("NO")