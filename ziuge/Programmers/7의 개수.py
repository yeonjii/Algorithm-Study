def solution(array):
    s_list = []
    for i in array:
        s_list.append(str(i))
    answer = 0
    for i in s_list:
        answer += i.count("7")
    
    return answer
