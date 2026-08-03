class Solution(object):
    def exclusiveTime(self, n, logs):
        results = [0] * n
        stack = []
        for log in logs:
            ID, status, time = log.split(":")
            ID, time = int(ID), int(time)
            if status == "start":
                stack.append((ID,time))
            else:
                ID, start = stack.pop()
                results[ID] += time - start +1
                if stack:
                    results[stack[-1][0]] -=time - start + 1
        return results