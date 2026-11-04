class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        number_str = str(n)
        res = 0
        while res not in numSet and res != 1:
            if res != 0:
                numSet.add(res)
                number_str = str(res)
                res = 0
            n_arr = []
            for c in number_str:
                n_arr.append(int(c))
            for n in n_arr:
                res += n**2           
            

        return True if res == 1 else False