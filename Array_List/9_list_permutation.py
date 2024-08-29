'''
List Permutation

Write a code to find whether the two given list are permutation of each other or not

input: list_permutation([1,2,3], [2,3,1])
output: True
'''

def list_permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    else:
        return False
    
print(list_permutation([1,2,3],[2,3,1]))