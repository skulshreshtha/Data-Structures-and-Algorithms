class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curString, openN, closeN):
            if len(curString) == 2 * n:
                res.append(curString)
            if openN < n:
                curString += "("
                backtrack(curString, openN+1, closeN)
                curString = curString[:-1]
            if closeN < openN:
                curString += ")"
                backtrack(curString, openN, closeN+1)
                curString = curString[:-1]
        
        backtrack("", 0, 0)
        return res