class Solution:
    def dailyTemperatures(self, temperatures):
        stack = list()
        ret = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append([temperatures[i],i])
                continue
            if stack[-1][0] >= temperatures[i]:
                stack.append([temperatures[i],i])
                continue
            while len(stack) and stack[-1][0] < temperatures[i]:
                item = stack.pop()
                ret[item[1]] = i - item[1]
            stack.append([temperatures[i],i])
        for item in stack:
            ret[item[1]] = 0
        return ret
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))