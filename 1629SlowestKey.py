class Solution(object):
    def slowestKey(self, rt, keysPressed):
        maxtime, idx = rt[0], 0
        for i in range(1, len(rt)):
            if rt[i]-rt[i-1] > maxtime:
                maxtime, idx = rt[i]-rt[i-1], i
            elif rt[i]-rt[i-1] == maxtime:
                if keysPressed[i] > keysPressed[idx]:
                    maxtime, idx = rt[i]-rt[i-1], i
        return keysPressed[idx]
