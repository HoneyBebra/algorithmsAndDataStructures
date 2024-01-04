def rocks(n_m: str) -> str:
    # https://new.contest.yandex.ru/48558/problem?id=215/2023_04_06/lX20wNIqZg

    n_m = n_m.split()
    n = int(n_m[0])
    m = int(n_m[1])

    if n % 2 == 0 and m % 2 == 0:
        return 'Loose'
    else:
        return 'Win'


def rocks_2(n_m: str) -> str:
    # https://new.contest.yandex.ru/48558/problem?id=215/2023_04_06/HFqqJtCCRh

    n_m = n_m.split()
    n = int(n_m[0])
    m = int(n_m[1])

    zero_coordinate = max(n, m) - min(n, m)
    if zero_coordinate % 3 == 0:
        return 'Loose'
    else:
        return 'Win'
