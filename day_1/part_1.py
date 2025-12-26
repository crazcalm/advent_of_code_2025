import fileinput

from dial import Dial


def main():
    dial = Dial(min=0, max=99, start=50)
    count = 0

    for line in fileinput.input():
        
        if line == "\n":
            break

        method = "decrement" if line.startswith("L") else "increment"
        turns = int(line[1:-1])

        for _ in range(turns):
            value = getattr(dial, method)()
    
        if value == 0:
            count += 1
        print(f"Input: {line[:-1]} -- dial: {value} -- Zero count: {count}")


if __name__ == "__main__":
    main()
    
