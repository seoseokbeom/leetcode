class Solution(object):
    def containsPattern(self, arr, m, k):
        cnt = 0
        for i in range(len(arr)-m):
            if arr[i] == arr[i+m]:
                cnt = cnt+1
                if(cnt == m*(k-1)):
                    return True
            else:
                cnt = 0
        return False
