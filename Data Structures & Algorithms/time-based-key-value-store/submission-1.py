class TimeMap:

    def __init__(self):
        # k: [(value, timestamp)]
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = [(value, timestamp)]
        else:
            self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val_list = []
        if key not in self.kv:
            return ""
        else:
            val_list = self.kv[key]
        l, r = 0, len(val_list) - 1
        res = ""
        while l <= r:
            mid = (l+r)//2
            mid_time = val_list[mid][1]
            if mid_time <= timestamp:
                res = val_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res