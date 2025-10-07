class RecentCounter:

    def __init__(self):
        self.RecentCounter = []   

    def ping(self, t: int) -> int:
        self.RecentCounter.append(t)
        count = 0
        i = len(self.RecentCounter)- 1

        while (self.RecentCounter[i] >= t - 3000) and i >= 0:
            count += 1
            i -= 1
        
        return count
    


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)