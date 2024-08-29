def findPairs(arr, target):
    seen = {}
    paris = []
    for idx, value in enumerate(arr):
        complement = target - value

        if complement in seen:
            paris.append([seen[complement], idx])
        
        seen[value] = idx
    return paris
arr = [1,2,3,2,3,4,5,6]
idx = [0,1,2,3,4,5,6,7]
target = 6
findPairs(arr, target)

'''
def findPairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]+arr[j] == target:
                pairs.append([i, j])
    return pairs

arr = [1,2,3,2,3,4,5,6]
target = 6
findPairs(arr, target)
'''