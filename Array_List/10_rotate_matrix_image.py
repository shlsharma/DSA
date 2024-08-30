'''
Rotate Matrix/ Image - LeetCode 48
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

Example:


Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
Output:         [[7,4,1],
                 [8,5,2],
                 [9,6,3]]
'''
import numpy as np

def rotate_matrix(matrix):
    matt = []
    for i in range(len(matrix)):
        mat = []
        for j in range(len(matrix)-1, -1, -1):
            mat.append(matrix[j][i])
        matt.append(mat)
    return matt

# def rotate_matrix(matrix):
#     matrix = np.array(matrix)
#     matrix = matrix.T
#     for i in range(np.shape(matrix)[0]):
#         temp = matrix[i][::-1]
#         matrix[i] = temp
#     return matrix

print(rotate_matrix([[1,2,3],
                 [4,5,6],
                 [7,8,9]]))