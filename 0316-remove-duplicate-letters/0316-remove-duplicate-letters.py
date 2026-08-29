class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        cnt = Counter(s)
        used = [False]*26

        for c in s:
            cnt[c]-=1
            if used[ord(c) - ord('a')]:
                continue
            while ans and ans[-1] > c and cnt[ans[-1]]>0:
                used[ord(ans[-1]) - ord('a')] = False
                ans.pop()
            ans.append(c)
            used[ord(c) - ord('a')] = True
        return "".join(ans)

        