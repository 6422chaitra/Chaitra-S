def merge_sorted_arrays_with_constraints(X, Y, m, n):
    # Validate inputs
    if not isinstance(X, list) or not isinstance(Y, list):
        raise TypeError("Both X and Y must be lists.")
    if m + n != len(X):
        raise ValueError("Length of X must be m + n.")
    if len(Y) != n:
        raise ValueError("Length of Y must be n.")

    # Last index of merged array
    last = m + n - 1
    i = m - 1  # Last valid element in X
    j = n - 1  # Last element in Y

    # Merge from the end to avoid overwriting
    while i >= 0 and j >= 0:
        if X[i] is not None and X[i] > Y[j]:
            X[last] = X[i]
            i -= 1
        else:
            X[last] = Y[j]
            j -= 1
        last -= 1

    # Copy remaining elements from Y (if any)
    while j >= 0:
        X[last] = Y[j]
        j -= 1
        last -= 1

    return X


# Example usage
if __name__ == "__main__":
    # X has 5 valid elements and 3 empty slots (None)
    X = [1, 3, 5, 7, 9, None, None, None]
    Y = [2, 6, 8]
    m = 5  # valid elements in X
    n = 3  # elements in Y

    merged = merge_sorted_arrays_with_constraints(X, Y, m, n)
    print("Merged array:", merged)
