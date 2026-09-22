class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for token in tokens:
            if token in {"+", "-", "*", "/"}:                      
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Division entière tronquée vers zéro (exigence LeetCode)
                    stack.append(int(a / b))
            else:
                # C'est un nombre, on l'ajoute à la pile
                stack.append(int(token))
                
        return stack[0]


            
            

        