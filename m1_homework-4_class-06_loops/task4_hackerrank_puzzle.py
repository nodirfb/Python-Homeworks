# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.

n = int(input())
for i in range(n):
    square = i * i
    print(square)