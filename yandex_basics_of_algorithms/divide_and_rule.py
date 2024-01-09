def lomuto_quicksort() -> str:
    array_count = int(input())
    array = list(map(int, input().split()))

    def lomuto_partition(arr: list, low: int, high: int) -> int:
        pivot = arr[low]
        i = low  # count elements are smaller than the pivot
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[i] = arr[i], arr[low]
        return i

    def recursion(arr: list, low: int, high: int) -> None:
        if low < high:
            count_under_pivot = lomuto_partition(arr=arr, low=low, high=high)
            recursion(arr=arr, low=low, high=count_under_pivot-1)
            recursion(arr=arr, low=count_under_pivot+1, high=high)

    recursion(arr=array, low=0, high=array_count-1)

    return ' '.join(str(item) for item in array)


def merge_sorted_arrays(count_arrays: int, arrays: list) -> str:
    result = []
    pointers = [0] * count_arrays

    while any(pointers[i] < len(arrays[i]) for i in range(count_arrays)):
        min_val = float('inf')
        min_index = -1

        for i in range(count_arrays):
            if pointers[i] < len(arrays[i]) and arrays[i][pointers[i]] < min_val:
                min_val = arrays[i][pointers[i]]
                min_index = i

        result.append(min_val)
        pointers[min_index] += 1

    return ' '.join(str(item) for item in result)
