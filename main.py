def min_time_to_make_equal(arr):
    max_val = max(arr)
    min_time = 0
    for num in arr:
        min_time += max_val - num
    return min_time
A = [2, 4, 1, 3, 2]
result = min_time_to_make_equal(A)
print("Minimum time in seconds:", result)
