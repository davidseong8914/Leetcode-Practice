class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            id_no, process, time = log.split(':')
            id_no, time = int(id_no), int(time)

            if process == "start":
                if stack: # there was a process already and we are intervening
                    res[stack[-1]] += time - prev_time
                stack.append(id_no)
                prev_time = time
            else: # process is ending
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        
        return res
