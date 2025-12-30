from pprint import pprint


if __name__ == "__main__":
    import fileinput
    import string
    from functools import reduce
    from itertools import zip_longest
    
    
    lines = list(fileinput.input())
    pprint(lines)

    problem = []
    operation = None
    total = 0
    
    for data in zip_longest(*lines):
        #print(data)
        if all([d in string.whitespace if d else False for d in data]):
            import pdb
            #pdb.set_trace()
            print(problem)
            if operation == "+":
                temp = sum(problem)
            elif operation == "*":
                temp = reduce(lambda x,y: x*y, problem)

            #print(temp)
            total += temp
            problem = []
            continue
        
        if data[-1] == "+" or data[-1] == "*":
            operation = data[-1]
        num = int("".join([x for x in data[:-1] if x and x.isdigit() ]))
        problem.append(num)
    pprint(problem)
    print(total)
