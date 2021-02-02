import sys

n = int(sys.stdin.readline())

numbers = sys.stdin.readline().rstrip()

sum_ = 0
for i in numbers:
    sum_ += int(i)
print(sum_)