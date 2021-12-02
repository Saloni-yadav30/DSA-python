///merge sort
def merge(arr,left,right):
    i=0 #index of 1st ele of left array
    j=0
    
    k=0 #storing array
    while i < len(arr) and j<len(arr):
        if left[i] < right[i]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[i]
            i+=1
        k+=1
        while i < len(arr):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(arr):
            arr[k]=right[j]
            j+=1
            k+=1
            

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        merge(arr,left,right)
        
arr=[23,52,71,10,14,90]
mergesort(arr)
print(arr)
