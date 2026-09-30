class Solution:
    def isValid(self, s: str) -> bool:
        # for each char in s -> add c to a stack
        # exemple if c ='(' -> pop from stack -> if next element from stack = closing bracket --> pop
        #if at the end no element in stack return true
        #else false
        #s = "({[]})"
        #stack ['(','{','[',']']
        stack = []
        closeToOpen = {'}':'{',')':'(',']':'['}
        if len(s)<2:
            return False
        for c in s:
            if c==')' or c==']' or c=='}':
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
            else:                    
                stack.append(c)
        return len(stack)==0  

   

        

        