from collections import defaultdict, deque


class TimeMap:

    def __init__(self):
        self.keystore = defaultdict[str, dict[int, str]](dict)
        self.recent = defaultdict[str, deque[tuple[int, str]]](deque)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key][timestamp] = value
        self.recent[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.keystore[key].get(timestamp, "")
        if res == "":
            recent = self.recent[key]
            for i in range(len(recent) - 1, -1, -1):
                if recent[i][0] <= timestamp:
                    return recent[i][1]
        return res


        
