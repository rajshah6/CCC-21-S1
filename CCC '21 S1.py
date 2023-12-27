n = int(input())
sum = 0
heights = [int(i) for i in input().split()]
lengths = [int(i) for i in input().split()]

for i in range(n):
    sum += lengths[i]*(heights[i]+heights[i+1])

print(sum / 2)
