'''
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''

def middle(lst):
    lst.pop(0) # o(n)
    lst.pop() # o(1)
    return lst

def middle(lst):
    return lst[1:-1] #o(n)

myList = [1, 2, 3, 4]
print(middle(myList))  # [2,3]

# space complexity is 0(n) as new list is returned