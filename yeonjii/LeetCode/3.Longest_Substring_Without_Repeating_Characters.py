# import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        q = collections.deque()
        for k in s:
            if k not in q:
                q.append(k)
            else:
                idx = q.index(k)
                for i in range(idx+1):
                    q.popleft()
                q.append(k)
            max_len = max(max_len, len(q))
        return max_len
