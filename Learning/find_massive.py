max = [2, 4, 1, 9, 5, 3, 6, 8]
a = len(max)
for i in range(a - 1):
    for i in range(a - 1):
        if max[i] > max[i + 1]:
            max[i], max[i + 1] = max[i + 1], max[i]

print(max)
