class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left=right=n
        res = []
        combo = ''
        self.generate(left,right,combo,res)
        return res
    
    def generate(self,left, right, combo, res):        
        if left:
            self.generate(left-1,right, combo+'(', res)
        if right>left:
            self.generate(left,right-1, combo+')', res)

        if left == 0 and right == 0:
            res.append(combo)
            return res