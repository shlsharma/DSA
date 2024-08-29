'''
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''

def remove_duplicates(lst):
    seen = {}

    for idx, value in enumerate(lst):
        seen[value] = idx
    
    return list(seen.keys())

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

# Time and Space complexity - o(n)