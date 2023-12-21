def upper_bound(lst:list[int],x:int)->int:
    lo,up=0,len(lst)-1
    while lo<up:
        mid=(lo+up)//2
        if x<lst[mid]:
            up=mid
        else:
            lo=mid+1
    return lo
if __name__=="__main__":
    lst=[1,2,2,2,2,2,3,4,5,10,11]
    print(upper_bound(lst,2))#output will be 6 as it has the upper bound index 5 and next element can be inserted at 6th index.