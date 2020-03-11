#You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        print("outer loop",temp,pos,val)
        pos += 1
      
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            print("inner loop",swaps,i,t,temp[i+1])
            temp[t] = temp[i+1]
    return swaps