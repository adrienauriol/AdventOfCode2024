import re 
import numpy as np 

def read_input(file_path):
    with open(file_path) as f:
        return "".join(f.read().splitlines())
    
def task1(input):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    matches = [(int(x) * int(y)) for x, y in matches]

    return np.sum(np.array(matches))

def task2(input):
    text = "Some text with mul(123,456), do() and don't() in it."
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, input)

    do = True

    result = 0

    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        
        if match[:3] == "mul":
            new_pattern = r"mul\((\d+),(\d+)\)"
            if do : 
                new_match = re.findall(new_pattern, match)
                tuple_new_match = new_match[0]
                result += int(tuple_new_match[0]) * int(tuple_new_match[1])

    return result

def main():
    input = read_input("data/day3.txt")
    result_task1 = task1(input)
    print("Task 1: ", result_task1)

    result_task2 = task2(input)
    print("Task 2: ", result_task2)

if __name__ == "__main__":
    main()
