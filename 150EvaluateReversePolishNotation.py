class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for v in tokens:
            if v not in ["+", "-", "/", "*"]:
                stack.append(v)
            else:
                a = stack.pop()
                b = stack.pop()
                print(b,v,a,'=',(eval(b+v+a)))
                stack.append(str(int(eval(b+v+a))))
                # print(a,b)
                print(stack)
        return stack[0]

a = Solution()
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
