class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens: 
            #print(stack)
            if(token == "+"):
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(c)
            elif(token == "-"):
                b = stack.pop()
                a = stack.pop()
                c = a - b
                stack.append(c)
            elif(token == "/"):
                b = float(stack.pop())
                a = float(stack.pop())
                c = int(a / b)
                stack.append(c)
            elif(token == "*"):
                b = stack.pop()
                a = stack.pop()
                c = a * b
                stack.append(c)
            else:
                stack.append(int(token))
        return stack[0]
        