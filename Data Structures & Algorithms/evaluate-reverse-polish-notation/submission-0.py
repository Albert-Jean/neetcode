class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        tempStack =[]
        while len(tokens) > 0:            
            print(tempStack, tokens)
            print(res)
            if tokens[0] != '+' or tokens[0] != '*' or tokens[0] != '/' or tokens[0] != '-':
                tempStack.append(tokens[0])
                tokens.pop(0)
            if tokens[0] == '+':
                tokens.pop(0)
                for n in tempStack:
                    res += int(n)
                tempStack=[]
            elif tokens[0] == '-':
                tokens.pop(0)
                for n in tempStack:
                    res -= int(n)
                tempStack=[]
            elif tokens[0] == '*':
                tokens.pop(0)
                for n in tempStack:
                    res *= int(n)
                tempStack=[]
            elif tokens[0] == '/': 
                tokens.pop(0)
                for n in tempStack:
                    res /= int(n)
                tempStack=[]
        return res


            
            

        