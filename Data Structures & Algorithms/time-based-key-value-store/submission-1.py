class TimeMap:

    def __init__(self):
        self.dicti = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dicti[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.dicti[key]
        if not values: return ""
        left = 0
        right = len(values) -1
        result = ""
        while left <= right:
            mid = (left+right)//2
            time = values[mid][1]
            if time == timestamp:
                return values[mid][0]
            elif time > timestamp:
                right = mid - 1
            else:
                result = values[mid][0]
                left = mid +1
        return result
