class Solution(object):
    def judgeCircle(self, moves):
        v = 0
        h = 0
        a = {}
        for val in moves:
            if(val == 'U'):
                v += 1
            elif(val == 'D'):
                v -= 1
            elif(val == 'L'):
                h -= 1
            elif(val == 'R'):
                h += 1
        if(v == 0 and h == 0):
            return True
        else:
            return False
