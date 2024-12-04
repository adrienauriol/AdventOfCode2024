import numpy as np

def read_input(path):
   data = np.loadtxt(path)
   return data

def task1(input):
    left_list = input[:,0]
    right_list = input[:,1]

    left_list = np.sort(left_list)
    right_list = np.sort(right_list)

    diff = abs(right_list - left_list)

    return diff.sum()

def task2(input):
    left_list = input[:,0]
    right_list = input[:,1]
    similarity_score = 0

    for element in left_list:
        for element2 in right_list:
            counter = 0
            if element == element2:
                counter += 1
            similarity_score += counter * element            

    return similarity_score


        
def main():
    input = read_input("data/day1.txt")
    result_task1 = task1(input)
    print("Task 1: ", result_task1)

    result_task2 = task2(input)
    print("Task 2: ", result_task2)

if __name__ == "__main__":
    main()