#include <stdio.h>

int main()
{
    int arr[6];
    for(int i=0 ; i<6 ;i++){
        printf("enter %d index element = ",i);
        scanf("%d",&arr[i]);
    }
    printf("the array before sorting is : \n");
    for(int i=0 ; i<6 ;i++){
        printf("%d ",arr[i]);
    }
    printf("\nthe array after sorting is :\n");
    for(int j=1 ; j<6 ; j++){
        int key = arr[j];
        int i = j-1;
        while (i>=0 && arr[i]>key) {
            arr[i+1]= arr[i];
            i=i-1;
        }
        arr[i+1]=key;
    }
    for(int i=0 ; i<6 ;i++){
        printf("%d ",arr[i]);
    }
}
