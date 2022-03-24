# TC(n+m*logn), where n = len(revenues) and m = len(milestones)
# SC(n)
def getMilestoneDays(revenues, milestones):
  
  def bs(nums, tar):
    i,j=-1,len(nums)
    
    while j-i >= 2 :
      mid=(i+j)//2 
      if nums[mid] < tar:
        i = mid
      else:
        j = mid
    return j
      
  run_sum=0
  res=[]
  ans=[]
  for x in revenues:
    run_sum+=x
    res.append(run_sum)
  for ms in milestones:
    ans.append(bs(res,ms)+1)
  return ans
