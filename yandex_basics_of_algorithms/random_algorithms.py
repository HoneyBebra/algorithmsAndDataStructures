import random


def random_lomuto_quicksort() -> str:
    array_count = int(input())
    array = list(map(int, input().split()))

    def lomuto_partition(arr: list, low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]  # swap places first and random element
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


print(random_lomuto_quicksort())
