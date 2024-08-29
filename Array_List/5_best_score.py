'''
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
'''

def best_score(lst):
    first_best = 0
    second_best = 0

    for score in lst:
        if score>first_best:
            second_best = first_best
            first_best = score
        elif score>second_best:
            second_best = score
    
    return first_best, second_best

# time complexity - o(n)
# space complexity - o(1)