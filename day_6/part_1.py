if __name__ == "__main__":
    import fileinput

    problems = {}
    total = 0
    
    for line in fileinput.input():
        line = line.strip()

        if not line:
            break

        values = [data for data in line.split(" ") if data]

        for index, data in enumerate(values):
            import pdb
            #pdb.set_trace()
            if index not in problems:
                problems[index] = [data]
            else:
                problems[index].append(data)

    for data in problems.values():
        operator = data[-1]
        result = 0 if operator == "+" else 1

        for value in data[:-1]:
            if operator == "+":
                result += int(value)
            elif operator == "*":
                import pdb
                #pdb.set_trace()
                result *= int(value)
                    
        total += result
    print(total)
