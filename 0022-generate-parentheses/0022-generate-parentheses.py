class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curAns = []
        def backtracking(openCount, closeCount):
            if len(curAns) == 2 * n:
                ans.append("".join(curAns))
            if closeCount < openCount:
                curAns.append(")")
                backtracking(openCount, closeCount+1)
                curAns.pop()
            if openCount < n:
                curAns.append("(")
                backtracking(openCount+1, closeCount)
                curAns.pop()
        backtracking(0, 0)
        return ans