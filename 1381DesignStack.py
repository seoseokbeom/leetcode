class CustomStack(object):

    def __init__(self, maxSize):
        self.stack = list()
        self.maxsize = maxSize
        self.currsize = 0
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.maxsize:
            self.stack.append(x)
            self.inc.append(0)
        # else:
        #     self.stack.push(x)
        #     self.currsize += 1

    def pop(self):
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


a = CustomStack(2)
# a(2)
a.push(2)
print()
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
