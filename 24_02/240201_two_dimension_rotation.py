def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]


two_dimension = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
new_array = []
for i in range(5):
    for j in range(5):
        new_array.append(two_dimension[i][j])

selectionSort(new_array, 25)
print(new_array)