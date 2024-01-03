def num_of_permutations(n: int) -> int:
    # https://new.contest.yandex.ru/48556/problem?id=215/2023_04_06/xAmHQ1PYv2

    res_num = 1
    for i in range(1, n + 1):
        res_num *= i
    return res_num


def count_of_choosing(n_k: str) -> int:
    # https://new.contest.yandex.ru/48556/problem?id=215/2023_04_06/yrA534pVxW

    # count of choosing algorithm:
    # C(n, k) = n! / (n!(n - k)!)
    # n - total number of objects in the set
    # k - number of choosing

    n_k = n_k.split()
    n = int(n_k[0])
    k = int(n_k[1])

    n_factorial = num_of_permutations(n)
    k_factorial = num_of_permutations(k)
    n_minus_k_factorial = num_of_permutations(n - k)

    return int(n_factorial / (k_factorial * n_minus_k_factorial))
