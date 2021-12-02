def partition(arr, p, r):
    pivot = arr[p]
    i = p
    for j in range(p+1,r+1):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[p],arr[i]=arr[i],arr[p]
    return i
            
def quicksort(arr , p , r):
    if p<r:
        q=partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)

arr= [6,4,1,5,2,3]
quicksort(arr,0,len(arr)-1)
print(arr)