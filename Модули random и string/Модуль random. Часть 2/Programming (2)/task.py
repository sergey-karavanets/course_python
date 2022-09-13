from random import shuffle

def shuffle_matrix(matrix):
    for lst in matrix:
        shuffle(lst)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

shuffle_matrix(matrix)