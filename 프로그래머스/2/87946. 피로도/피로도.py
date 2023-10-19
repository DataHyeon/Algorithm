def solution(current_stamina, dungeons):
    if not dungeons:
        return 0

    max_explored = 0
    for i, (requirement, fatigue) in enumerate(dungeons):
        if current_stamina >= requirement:
            new_dungeons = dungeons[:i] + dungeons[i+1:]
            explored = 1 + solution(current_stamina - fatigue, new_dungeons)
            max_explored = max(max_explored, explored)

    return max_explored