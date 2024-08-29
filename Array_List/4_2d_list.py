'''
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(myList2D) # 15
'''

def sum_diag(lst):
    lst_diag = [lst[i][i] for i in range(len(lst))]
    return sum(lst_diag)

print(sum_diag([[1,2,3],[4,5,6],[7,8,9]]))

# time complexity - o(n)
# space complexity - o(1)