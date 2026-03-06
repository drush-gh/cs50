class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if n < 0 or not str(n).isdigit():
            raise ValueError("Deposit amount must be a non-negative integer")
        if (n + self.size) <= self.capacity:
            self.size += n
        else:
            raise ValueError("Amount will exceed Jar capacity")

    def withdraw(self, n):
        if n < 0 or not str(n).isdigit():
            raise ValueError("Withdraw amount must be a non-negative integer")
        if (self.size - n) >= 0:
            self.size -= n
        else:
            raise ValueError("Jar size is less than withdraw amount")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or not str(capacity).isdigit():
            raise ValueError("Capacity of Jar must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity or not str(size).isdigit():
            raise ValueError("Size of Jar must be a non-negative integer that is less than or equal to Jar capacity")
        self._size = size


















def main():
    jar1 = Jar(10)
    print(jar1.capacity)
    #jar1.size = 0
    print(jar1.size)

    jar1.size = 10


    jar2 = Jar(50)
    jar2.size = 15
    print(f"Jar 2 Size: {jar2.size}")
    print(f"Jar 1: {jar1}")
    print(f"Jar 2: {jar2}")

    jar1.withdraw(5)
    jar2.deposit(5)
    print(f"Jar 1: {jar1}")
    print(f"Jar 2: {jar2}")



if __name__ == "__main__":
    main()
