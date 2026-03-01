import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Array:\n", arr)

print("Row sums:", np.sum(arr, axis=1))
print("Column sums:", np.sum(arr, axis=0))

flat = arr.flatten()
flat.sort()
print("Second maximum element:", flat[-2])