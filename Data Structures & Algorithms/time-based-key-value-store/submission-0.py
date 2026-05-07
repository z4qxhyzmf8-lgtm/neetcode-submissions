class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash:
            self.hash[key].append([value, timestamp])
        else:
            self.hash[key] = []
            self.hash[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hash:
            return ''
        if self.hash[key][0][1] > timestamp:
            return ''
        n = len(self.hash[key])
        l = 0
        r = n - 1
        val = self.hash[key][0]
        while l <= r:
            mid = (l + r) // 2
            if self.hash[key][mid][1] == timestamp:
                return self.hash[key][mid][0]
            if self.hash[key][mid][1] > timestamp:
                r = mid - 1
            else:
                val = self.hash[key][mid][0]
                l = mid + 1
        return val

        
