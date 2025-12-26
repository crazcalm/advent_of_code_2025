def shift(data, value, index):
    shifted = None
    while index < len(data):
        if data[index][0] <= value[0] and data[index][1] > value[1]:
            # edge case: need to make sure I am not shifting the value past other values with a later index...
            if index > 1:
                if data[index-1][1] > value[1]:
                    break
            shifted = data[index]
            data[index] = value
            break
        index+=1
    return shifted

def batteries(data, spaces=12):
    data = [int(c) for c in data]
    original_len = len(data)
    result = []
    for num in range(spaces):
        result.insert(0, (data.pop(), original_len - num - 1))
    print(result)
    for ix, digit in enumerate(reversed(data), start=spaces + 1):
        import pdb
        #pdb.set_trace()
        for index in range(spaces):
            if digit >= result[index][0]:
                value = result[index]
                result[index] = (digit, original_len - ix)

                while value and index < spaces and value[1] > result[index][1]:
                    index +=1
                    value = shift(result, value, index)
                break
            else:
                break
        print(result)
    return int("".join([str(d) for d,i in result]))
        
        
              

if __name__ == "__main__":
    import fileinput
    count = 0
    for line in fileinput.input():
        line = line.strip()
        if not line:
            break
        import pdb
       # pdb.set_trace()
        result = batteries(line)
        count += result
        
        print(f"{line} => {result}")

    print(count)
