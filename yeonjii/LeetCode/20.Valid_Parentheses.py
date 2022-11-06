class Solution:
    def isValid(self, s: str) -> bool:
        ans = True
        stack = []
        for k in list(s):
            if k == '(' or k == '{' or k == '[':  # 여는 괄호인 경우
                stack.append(k)
            elif len(stack) != 0:
                if (k == ')' and stack[-1] == '(') or (k == '}' and stack[-1] == '{') or (
                        k == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    ans = False
                    break
            else:
                ans = False
                break
        if len(stack) != 0:
            ans = False

        return ans