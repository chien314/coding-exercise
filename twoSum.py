def twoSum(srr, tar):
    arr.sort()
    i,j = 0,len(arr)-1
    while i<j:
        su = arr[i]+arr[j]
        if su == tar:
            return i,j
        elif su < tar:
            i+=1
        else:
            j-=1
    return -1
 
# return number
def threeSum(arr, tar):

  arr.sort()
  for k in range(len(arr)-2):
      i,j = k+1,len(arr)-1

      while i<j:
          su = arr[i]+arr[j]+arr[k]
          if su == tar:
              return arr[k],arr[i],arr[j]
          elif su < tar:
              i+=1
          else:
              j-=1
  return -1

# return index
def threeSum_idx(arr, tar):
    for i, n in enumerate(arr):
        arr[i]=(i,n)
        
    arr.sort(key = lambda x: x[1])
#     print(arr)
    for k in range(len(arr)-2):
        i,j = k+1,len(arr)-1

        while i<j:
            su = arr[i][1]+arr[j][1]+arr[k][1]
            if su == tar:
                return arr[i][0],arr[j][0],arr[k][0]
            elif su < tar:
                i+=1
            else:
                j-=1
    return -1
