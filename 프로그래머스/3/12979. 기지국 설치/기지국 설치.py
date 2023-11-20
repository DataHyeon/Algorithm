def solution(N, stations, W):
    # 필요한 추가 기지국 수
    additional_stations = 0

    # 현재 커버되지 않은 아파트의 시작 위치
    start = 1

    for station in stations:
        # 기지국 전파의 시작 지점
        left = station - W
        # 기지국 전파의 끝 지점
        right = station + W

        # 현재 커버되지 않은 구간에 대해 필요한 기지국 수 계산
        if start < left:
            # 전파가 도달하지 않는 구간의 길이
            uncovered_length = left - start
            # 구간에 필요한 기지국 수
            additional_stations += (uncovered_length + (2 * W)) // (2 * W + 1)

        # 다음 커버되지 않은 아파트의 시작 위치 업데이트
        start = right + 1

    # 마지막 기지국 이후의 구간에 대해 필요한 기지국 수 추가 계산
    if start <= N:
        uncovered_length = N - start + 1
        additional_stations += (uncovered_length + (2 * W)) // (2 * W + 1)

    return additional_stations