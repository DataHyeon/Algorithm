def solution(routes):
    # 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    cameras = 1  # 최소 하나의 카메라는 설치해야 함
    camera_position = routes[0][1]  # 첫 번째 차량의 진출 지점에 카메라 설치

    for route in routes:
        # 현재 카메라 위치가 차량의 진입 지점보다 앞에 있는 경우, 새로운 카메라 설치 필요
        if camera_position < route[0]:
            cameras += 1
            camera_position = route[1]  # 새로운 카메라 위치 업데이트

    return cameras