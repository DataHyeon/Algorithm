def solution(word):
    answer = 0
    
    word_list = ["A", "E", "I", "O", "U"]
    check_dict = {_ : [] for _ in range(1,6)}
    test_word = ''
    
    for a in word_list:
        check_num = 1
        if test_word == word:
            return answer
        if len(test_word) >= 1:
            test_word = test_word[:0]
        if test_word == word:
            return answer
        if len(test_word) == 0:
            test_word += a
            answer += 1
            check_dict[check_num].append(a)
        # if len(check_dict[check_num+1]) == 5:
        #     continue
        
        for b in word_list:
            check_num = 2
            if test_word == word:
                return answer
            if len(test_word) >= 2:
                test_word = test_word[:1]
            if test_word == word:
                return answer
            if len(test_word) == 1:
                test_word += b
                answer += 1
                check_dict[check_num].append(b)
            # if len(check_dict[check_num+1]) == 5:
            #     continue
            
            for c in word_list:
                check_num = 3
                if test_word == word:
                    return answer
                if len(test_word) >= 3:
                    test_word = test_word[:2]
                if test_word == word:
                    return answer
                if len(test_word) == 2:
                    test_word += c
                    answer += 1
                    check_dict[check_num].append(c)
                # if len(check_dict[check_num+1]) == 5:
                #         continue
                
                for d in word_list:
                    check_num = 4
                    if test_word == word:
                        return answer
                    if len(test_word) >= 4:
                        test_word = test_word[:3]
                    if test_word == word:
                        return answer
                    if len(test_word) == 3:
                        test_word += d
                        answer += 1
                        check_dict[check_num].append(d)
                    # if len(check_dict[check_num+1]) == 5:
                    #     continue
                    
                    for f in word_list:
                        check_num = 5
                        if test_word == word:
                            return answer
                        if len(test_word) == 5:
                            test_word = test_word[:4]
                        if test_word == word:
                            return answer
                        if len(test_word) == 4:
                            test_word += f
                            answer += 1
                            check_dict[check_num].append(f)
    return answer