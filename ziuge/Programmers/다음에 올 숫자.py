def solution(common):
    answer = 0
    
    if common[1] - common[0] == common[2] - common[1] :
        temp = common[1] - common[0]
        answer = common[-1] + temp
    else:
        temp = common[1] // common[0]
        answer = common[-1] * temp
    
    return answer
