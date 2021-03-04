#  Write a Python function to check whether a number is in a given range
def check(n):
    if n in range(1,10):
        return print("in this range")
    else:
        return print("not")

n = int(input("program will check if number is in range between 1 and 10 "))

check(n)