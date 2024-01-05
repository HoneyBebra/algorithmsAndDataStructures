def selection_sort(n: int, array: str) -> str:
    # https://new.contest.yandex.ru/48569/problem?id=215/2023_04_06/08fmDTMXQZ

    array = array.split()
    array = [int(i) for i in array]

    for i in range(n):
        min_array = min(array[i:])
        array[array.index(min_array)], array[i] = array[i], min_array

    return ' '.join(str(i) for i in array)
