from itertools import permutations

def match(banned_id, user_id):
    if len(banned_id) != len(user_id):
        return False
    for b, u in zip(banned_id, user_id):
        if b != '*' and b != u:
            return False
    return True

def solution(user_id, banned_id):
    possible_combinations = set()

    for perm in permutations(user_id, len(banned_id)):
        if all(match(b, u) for b, u in zip(banned_id, perm)):
            possible_combinations.add(tuple(sorted(perm)))

    return len(possible_combinations)