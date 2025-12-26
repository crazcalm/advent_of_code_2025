class Dial:
    def __init__(self, min=0, max=99, start=0):
        self._value = start
        self.min = min
        self.max = max

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, data):
        if data < self.min:
            self._value = self.max
        elif data > self.max:
            self._value = self.min
        else:
            self._value = data

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

if __name__ == "__main__":
    import fileinput
    dial = Dial(min=0, max=99, start=50)
    count = 0

    for line in fileinput.input():
        if line == "\n":
            break
        
        method = None
        if line.startswith("L"):
            method = "decrement"
        else:
            method = "increment"

        turns = int(line[1:-1])

        for _ in range(turns):
            value = getattr(dial, method)()
            if value == 0:
                count += 1
        print(value, count)
