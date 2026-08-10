class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.my_arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.my_arr[i]

    def set(self, i: int, n: int) -> None:
        self.my_arr[i] = n

    def pushback(self, n: int) -> None:
        if (self.size == self.capacity):
            self.resize()

        self.my_arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.my_arr[self.size - 1]
        self.my_arr[self.size - 1] = 0
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [0] * self.capacity

        for i in range(len(self.my_arr)):
            newArr[i] = self.my_arr[i]
        
        self.my_arr = newArr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
