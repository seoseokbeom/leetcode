class Solution(object):
    def freqAlphabets(self, s):
        a = s.replace("10#", "j").replace("11#", "k")
        .replace("12#", "l")
        .replace("13#", "m")
        .replace("14#", "n")
        .replace("15#", "o")
        .replace("16#", "p")
        .replace("17#", "q")
        .replace("18#", "r")
        .replace("19#", "s")
        .replace("20#", "t")
        .replace("21#", "u")
        .replace("22#", "v")
        .replace("23#", "w")
        .replace("24#", "x")
        .replace("25#", "y")
        .replace("26#", "z")
        .replace("1", "a")
        .replace("2", "b")
        .replace("3", "c")
        .replace("4", "d")
        .replace("5", "e")
        .replace("6", "f")
        .replace("7", "g")
        .replace("8", "h")
        .replace("9", "i")
        return a

    def freqAlphabets(self, s):
        arr = []
        start = 0
        for i, v in enumerate(s):
            if v == "#":
                arr.append(s[start:i+1])
                start = i+1
            elif i == len(s)-1:
                arr.append(s[start:])
        arr2 = []
        for i, v in enumerate(arr):
            if v[-1] == '#':
                for j in range(len(v)-3):
                    arr2.append(v[j])
                arr2.append(v[-3:])
            else:
                for v2 in v:
                    arr2.append(v2)
        res = ""
        for i, v in enumerate(arr2):
            if len(v) == 1:
                res += chr(96+int(v))
            else:
                res += chr(96+int(v[:-1]))
        return res


a = Solution()
print(a.freqAlphabets(s="10#11#12"))
