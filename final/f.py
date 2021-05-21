import math
nums = list(set(input().split()))
answer = []
for i in nums:
    if not math.log2(int(i)).is_integer():
        answer.append(int(i))
answer.sort()
print(*answer, sep = " ")