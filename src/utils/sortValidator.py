def is_sorted(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False

    return True
