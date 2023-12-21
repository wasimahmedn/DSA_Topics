def upper_bound(lst:list[int],x:int)->int:
    lo,up=0,len(lst)-1
    while lo<up:
        mid=(lo+up)//2
        if x<lst[mid]:
            up=mid
        else:
            lo=mid+1
    return lo


def min_obslt_sum_diff(nums1,nums2,n):
    obslt_diff=[]
    for i in range(n):
        obslt_diff.append(abs(nums1[i]-nums2[i]))
    
    nums1.sort()
    best_diff=[]
    for i in range(n):
        pos=upper_bound(nums1,nums2[i])
        if pos>0 and pos<n:
            best_diff.append(min(abs(nums1[pos]-nums2[i]),abs(nums1[pos-1]-nums2[i])))
        elif pos==0:
            best_diff.append(abs(nums1[0]-nums2[i]))
        elif pos>=n:
            best_diff.append(abs(nums1[n-1]-nums2[i]))
    
    mx=0
    for i in range(n):
        mx=max(mx,abs(obslt_diff[i]-best_diff[i]))
    return abs(sum(obslt_diff)-mx)%(pow(10,9)+7)

nums1 = [1,7,5] 
nums2 = [2,3,5]
print(min_obslt_sum_diff(nums1,nums2,len(nums1)))
nums1 = [2,4,6,8,10]
nums2 = [2,4,6,8,10]
print(min_obslt_sum_diff(nums1,nums2,len(nums1)))
nums1 = [1,10,4,4,2,7]
nums2 = [9,3,5,1,7,4]
print(min_obslt_sum_diff(nums1,nums2,len(nums1)))
# print()

