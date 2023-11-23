def solution(people, limit):
    # 정렬
    people.sort()
    start, end = 0, len(people) - 1
    boats = 0

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        # 두 명을 짝지우지 못한 경우 제일 무거운 사람 1명씩 내보냄
        end -= 1
        boats += 1

    return boats