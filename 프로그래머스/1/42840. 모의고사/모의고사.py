def solution(answers):
    collect_dict = {1: 0, 2: 0, 3: 0}
    p_answer_dict = {
        1: [1,2,3,4,5],
        2: [2,1,2,3,2,4,2,5],
        3: [3,3,1,1,2,2,4,4,5,5]
    }
    
    for p, p_a in p_answer_dict.items():
        for idx, answer in enumerate(answers):
            if answer == p_a[idx % len(p_a)]:
                collect_dict[p] += 1
    
    max_score = max(collect_dict.values())
    result = list(map(lambda x: x[0], filter(lambda x: x[1] == max_score, collect_dict.items())))
    
    return result
