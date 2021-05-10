class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        m = {'2':"abc"
            ,'3':"def"
            ,'4':"ghi"
            ,'5':"jkl"
            ,'6':"mno"
            ,'7':"pqrs"
            ,'8':"tuv"
            ,'9':"wxyz"}
        
        ans = []
        if len(digits) == 0:
            return ans
        
        def backtrack(ans, m, combination, index, digits):
            if(index > len(digits)):
                return
            if(len(combination) == len(digits)):
                ans.append(combination)
                return
            cur_string = m.get(digits[index],"")
            for char in cur_string:
                backtrack(ans, m, combination+char,index+1, digits)
                
                
        backtrack(ans,m, "", 0, digits)
        
        return ans