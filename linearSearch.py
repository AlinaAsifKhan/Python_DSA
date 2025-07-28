def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [1,2,4,5,7,8]
target = 11
res = linearSearch(arr,target)
if res==-1:
    print("not found")
else:
    print(f"found at index {res}")