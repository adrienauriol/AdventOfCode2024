import numpy as np
import re

def read_input(path):
   data = np.loadtxt(path)
   return data

def task1(input):
    pass

def task2(input):
    pass
        
def main():
    input = read_input("data/dayN.txt")
    # input = read_input("data/dayN_test.txt")

    result_task1 = task1(input)
    print("Task 1: ", result_task1)

    result_task2 = task2(input)
    print("Task 2: ", result_task2)

if __name__ == "__main__":
    main()