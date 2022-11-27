class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        elif n==2:
            return ["()()", "(())"]
        dp = [["()"], ["()()", "(())"]]
        for i in range(3,n+1):
            tmp = []
            for j in dp[-1]:
                for k in range(len(j)):
                    if not j[:k]+"()"+j[k:] in tmp:
                        tmp.append(j[:k]+"()"+j[k:])
            dp.append(tmp)
        return dp[-1]
