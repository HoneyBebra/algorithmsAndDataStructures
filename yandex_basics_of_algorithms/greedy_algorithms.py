def booking_a_meeting_room():
    # https://new.contest.yandex.ru/48557/problem?id=215/2023_04_06/RdGbbmsLQn

    count = int(input())
    bookings = []
    for i in range(count):
        start_end = input().split()
        bookings.append(start_end)

    res = 0
    while True:
        try:
            min_end = min([int(start_end[1]) for start_end in bookings])
            bookings = [start_end for start_end in bookings if int(start_end[0]) > min_end]
            res += 1
        except ValueError:
            break

    return res
