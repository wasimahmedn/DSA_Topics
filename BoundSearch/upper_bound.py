def upper_bound(lst:list[int],x:int)->int:
    lo,up=0,len(lst)-1
    while lo<up:
        mid=(lo+up)//2
        if x<lst[mid]:
            up=mid
        else:
            lo=mid+1
    return lo