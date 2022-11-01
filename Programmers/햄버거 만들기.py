# Lv. 1
# 햄버거 만들기
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

def solution(ingredient):
    answer = 0
    stack = ingredient[:3]

    for i in range(3, len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1] :
            answer += 1
            # 시간 초과.. 시간복잡도 n일텐데 for문 써서 그런가
            # stack = stack[:-4] <- 요부분이 문제였음!
            for j in range(4):
                stack.pop() # 요렇게 바꿔주니 해결!
    
    return answer
