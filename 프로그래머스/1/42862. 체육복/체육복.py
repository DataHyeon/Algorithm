def solution(n, lost, reserve):
    # 자신의 체육복을 도난당한 학생 처리
    reserve_only = [r for r in reserve if r not in lost]
    lost_only = [l for l in lost if l not in reserve]

    # 여벌 체육복이 있는 학생이 체육복을 빌려줄 수 있는지 확인
    for r in sorted(reserve_only):
        # 바로 앞 번호의 학생에게 빌려줄 수 있는 경우
        if r - 1 in lost_only:
            lost_only.remove(r - 1)
        # 바로 뒷 번호의 학생에게 빌려줄 수 있는 경우
        elif r + 1 in lost_only:
            lost_only.remove(r + 1)

    # 체육수업을 들을 수 있는 학생 수 계산
    answer = n - len(lost_only)
    return answer