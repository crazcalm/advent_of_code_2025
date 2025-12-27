import fileinput

from invalid_id import InvalidIds


def starts_with_0(data):
    if data.startswith("0"):
        return True
    else:
        return False

    
def repeat_twice(num):
    data = str(num)
    half = len(data) // 2
    return data[:half] == data[half:]


def main():
    result = 0
    for line in fileinput.input():
        if line == "\n":
            break
        
        for ranges in line.split(","):
            start, stop = ranges.split("-")

            for id_ in InvalidIds(int(start), int(stop), checks=[repeat_twice]):
                print(f"Invalid ID: {id_}")
                result += id_

    print(f"Sum of invalid ids: {result}")


if __name__ == "__main__":
    main()
    
