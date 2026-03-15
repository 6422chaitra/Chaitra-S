def find_index_of_zero(arr):
    max_count = 0       # Maximum length of continuous 1s found so far
    max_index = -1      # Index of zero to replace
    prev_zero = -1      # Index of previous zero
    prev_prev_zero = -1 # Index of zero before the previous zero

    for i, val in enumerate(arr):
        if val == 0:
            # Update the zero positions
            prev_prev_zero = prev_zero
            prev_zero = i

        # Calculate the length of the current sequence of 1s with at most one zero replaced
        if i - prev_prev_zero > max_count:
            max_count = i - prev_prev_zero
            max_index = prev_zero

    return max_index


# Example usage
if __name__ == "__main__":
    try:
        # Example binary array
        arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
        
        # Validate input
        if not all(x in (0, 1) for x in arr):
            raise ValueError("Array must contain only 0s and 1s.")
        
        index = find_index_of_zero(arr)
        if index != -1:
            print(f"Replace 0 at index {index} to get the longest sequence of 1s.")
        else:
            print("No zero found in the array.")
    except Exception as e:
        print(f"Error: {e}")
