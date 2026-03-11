def has_pair_with_sum_brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
            return False
        
# Example Usage
arr = [0, -1, 2, -3, 1]
target = -2
print(has_pair_with_sum_brute_force(arr, target)) 