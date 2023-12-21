def lower_bound(lst:list[int],x:int)->int:
    lo,up=0,len(lst)-1
    while lo<up:
        mid=(lo+up)//2
        if x<=lst[mid]:
            up=mid
        else:
            lo=mid+1
    return lo


if __name__=="__main__":
    lst=[1,2,2,2,2,2,2,2,3,10,11,19,20,22]
    print(lower_bound(lst,2))# The output will be 1 as the lower bound of 2 in lst in 1.