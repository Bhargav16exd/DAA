arr = [1,2,3,4,5,6,7,8,9,10]
val = 11

def binarySearch(arr,low,high,value):

    mid = (low + high) // 2

    if low == high: 
      if arr[mid] == value:
         return 1
      else:
         return 0
    else:
        if arr[mid] == value  :
            return 1
        elif arr[mid] > value : 
           return binarySearch(arr,low,mid,value)
        elif arr[mid] < value :
           return binarySearch(arr,mid+1,high,value)
        


n = len(arr)
element = binarySearch(arr,0,n-1,val)


