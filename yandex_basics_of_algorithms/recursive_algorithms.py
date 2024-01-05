def hanoi_towers(n: int) -> None:
    # https://new.contest.yandex.ru/48568/problem?id=215/2023_04_06/DEEgnJVwi3

    print(2**n - 1)

    def recursion(n_inner: int, from_peg: int, to_peg: int) -> None:
        if n_inner == 1:
            print(f'{from_peg} {to_peg}')
            return
        unused_peg = 6 - from_peg - to_peg

        recursion(n_inner=n_inner-1, from_peg=from_peg, to_peg=unused_peg)
        print(f'{from_peg} {to_peg}')
        recursion(n_inner=n_inner-1, from_peg=unused_peg, to_peg=to_peg)

    recursion(n_inner=n, from_peg=1, to_peg=3)


hanoi_towers(3)
