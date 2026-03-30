class MinStack:
    def __init__(self):
        self.storage = []

    def push(self, val: int) -> None:
        self.storage.append(val)

    def pop(self) -> None:
        self.storage.pop()

    def top(self) -> int:
        if len(self.storage) <= 0:
            return 0
        return self.storage[len(self.storage) - 1]

    def getMin(self) -> int:
        if len(self.storage) <= 0:
            return 0
        return min(self.storage)

