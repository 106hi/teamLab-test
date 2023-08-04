n = int(input())
count = 0
for num in range(1, (n + 1), 2):
    count += num ** 3
print(count)