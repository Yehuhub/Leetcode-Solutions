
# my solution:

class TimeMap:

    def __init__(self):
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.times:
            self.times[key].append((timestamp, value))
        else:
            self.times[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""

        l,r = 0, len(self.times[key]) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.times[key][mid][0] == timestamp:
                return self.times[key][mid][1]
            
            if self.times[key][mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1


        if l-1 >= 0:
            return self.times[key][l-1][1]
        return ""



# a slightlt cleaner solution
# the difference is we keep a res string in which we always update it if the mid val is samller than
# the one we are looking for
class TimeMap:

    def __init__(self):
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.times:
            self.times[key].append((timestamp, value))
        else:
            self.times[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.times.get(key, [])

        l,r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] == timestamp:
                return self.times[key][mid][1]
            
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                res = values[mid][1]
                l = mid + 1

        return res