from collections import Counter

def solution(topping):
    answer = 0

    # 형, 동생 토핑 리스트
    a = {}
    b = Counter(topping)

    for i in range(len(topping)):
        if topping[i] in a:
            a[topping[i]] += 1
        else:
            a[topping[i]] = 1

        b[topping[i]] -= 1

        if b[topping[i]] == 0:
            del b[topping[i]]

        if len(a) == len(b):
            answer += 1

        # temp = b.popleft()
        # a.append(temp)
        # a_topping = Counter(a).keys()
        # b_topping = Counter(b).keys()
        # if len(a_topping) == len(b_topping):
        #     answer += 1


        # a_topping = set(a)
        # b_topping = set(b)
        # if len(a_topping) == len(b_topping):
        #     answer += 1



    return answer
