import numpy as np 
import re

def read_input(file_path):
    data = np.loadtxt(file_path, dtype=str)
    table = np.array([list(row) for row in data])
    return table

def search_by_line(crossword, word):
    count = 0
    for row in crossword:
        row_str = "".join(row)
        count += len(re.findall(word, row_str))
    return count

def search_by_diagonal(crossword, word):
    diagonals_collection = []
    diagonals_collection.append(crossword.diagonal())
    diagonals_collection.append(np.diagonal(np.flipud(crossword)))
    length = crossword.shape[0]
    for i in range(1,length):
        diagonals_collection.append(np.diagonal(crossword, offset=i))
        diagonals_collection.append(np.diagonal(crossword, offset=-i))
        diagonals_collection.append(np.diagonal(np.flipud(crossword), offset=i))
        diagonals_collection.append(np.diagonal(np.flipud(crossword), offset=-i))

    # Now search for word in all possible diagonals
    count = 0
    for possible_diag in diagonals_collection:
        diag_str = "".join(possible_diag)
        count += len(re.findall(word, diag_str))

    return count

def check_corners(position, crossword):
    row_A, column_A = position
    
    upleft_corner = crossword[row_A-1][column_A-1]
    upright_corner = crossword[row_A-1][column_A+1]
    botleft_corner = crossword[row_A+1][column_A-1]
    botright_corner = crossword[row_A+1][column_A+1]

    if (upleft_corner != "M" and upleft_corner != "S") : return False
    if (upright_corner != "M" and upright_corner != "S") : return False
    if (botleft_corner != "M" and botleft_corner != "S") : return False
    if (botright_corner != "M" and botright_corner != "S") : return False
    if (upleft_corner == botright_corner) : return False
    if (botleft_corner == upright_corner) : return False

    return True
    
def task1(input):
    horizontal_occurences_leftright = search_by_line(input, "XMAS")
    horizontal_occurences_rightleft = search_by_line(input, "SAMX")
    vertical_occurences_updown = search_by_line(input.T, "XMAS")
    vertical_occurences_downup = search_by_line(input.T, "SAMX")
    diagonal_occurences_leftright = search_by_diagonal(input, "XMAS")
    diagonal_occurences_rightleft = search_by_diagonal(input, "SAMX")

    return horizontal_occurences_leftright + horizontal_occurences_rightleft + vertical_occurences_updown + vertical_occurences_downup + diagonal_occurences_leftright + diagonal_occurences_rightleft

def task2(input):
    counter = 0
    # First need to loop on all possible "center" of X and check if it is a A. 
    for i,row in enumerate(input[1:-1]) :
        for j,element in enumerate(row[1:-1]) : 
            if element == "A" : # candidate for a X-MAS. Need to check the corners
                row_a = i+1
                column_a = j+1
                counter+= check_corners((row_a,column_a),input)

    return counter




def main():
    input = read_input("data/day4.txt")
    # input = read_input("data/day4_test.txt")

    result_task1 = task1(input)
    print("Task 1: ", result_task1)

    result_task2 = task2(input)
    print("Task 2: ", result_task2)

if __name__ == "__main__":
    main()
