def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[10,30,20,40,60,50]
bubblesort(arr)
for v in arr:
    print(v)