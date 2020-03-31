def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        least = i
        for j in range(i,n):
          if(arr[least]>arr[j]):
            least=j
        arr[i],arr[least]=arr[least],arr[i]

    return arr

"""=========================================================="""

def Insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

"""=========================================================="""

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

"""=========================================================="""

def shell_sort(arr):
    h=len(arr)//2
    while h>0:
        for i in range(h,len(arr)):
            j=i
            while j>=h and arr[j] < arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j-=h
        h //=2
        
    return arr

"""=========================================================="""

def partition(arr, left, right):
    pivot = arr[left] # make the first element as pivot 
    i=left+1
    j=right
    while(1):
      while(i<=right and arr[i]<pivot):
        i+=1
      while(j>left and arr[j]>pivot):
        j-=1
      if(j<=i):
        break
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j-=1
    arr[left],arr[j]=arr[j],arr[left]

    return j

def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p-1) # sorts the left side of pivot 
        quick_sort(arr, p + 1, right) # sort the right side of pivot.

    return arr

"""=========================================================="""

def merge(arr,left,right):
    i=0
    j=0
    for k in range(len(arr)):
      if(i>=len(left)):
        arr[k]=right[j]
        j+=1
      elif(j>=len(right)):
        arr[k]=left[i]
        i+=1
      elif(left[i]>right[j]):
        arr[k]=right[j]
        j+=1
      else:
        arr[k]=left[i]
        i+=1
    return arr

def merge_sort(arr):
    n = len(arr)

    if n > 1:
        # find the mid point
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # sort the left and right part
        merge_sort(left)
        merge_sort(right)
        # merge
        arr=merge(arr,left,right)
    return arr

"""=========================================================="""
"""
def heap_sort(arr):
    n=len(arr)
    heap=MaxHeap(n)

    for i in arr:
        heap.add(i)

    for i in range(n,0,-1):
        arr[i]=heap.pop()

    return arr

def downheap(i,size):
    while (2*i + 1)<= size:
        k = 2*i +1
        if (k < size-1) and (arr[k] < arr[k+1]):
            k+=1
        if(arr[i] >= arr[k]):
            break
        arr[i], arr[k] = arr[k], arr[i]
        i = k


def heapify(arr):
    hsize = len(arr)
    for i in range(hsize//2 -1, -1, -1):
        downheap(i,hsize)

def Heap_sort(arr):
    n=len(arr)
    for i in range(n):
        arr[0], arr[n-1] = arr[n-1], arr[0]
        downheap(0,n-2)
        n-=1
"""

# 2-1.  Implement (a) selection sorting (b) quick sorting and (c) merge sorting
def main():
    arr = [5, 3, 8, 4, 9 , 1, 6, 2, 7]
    print("selection sort", selection_sort(arr))
    arr = [5, 3, 8, 4, 9 , 1, 6, 2, 7]
    print("insertion sort", Insertion_sort(arr))
    arr = [5, 3, 8, 4, 9 , 1, 6, 2, 7]
    print("Bubble sort", bubble_sort(arr))
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Shell sort", shell_sort(arr))
    arr = [5, 3, 8, 4, 9 , 1, 6, 2, 7]
    print("quick sort", quick_sort(arr, left = 0 , right = len(arr) - 1))
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("merge sort", merge_sort(arr))
    #arr = [38, 27, 43, 3, 9, 82, 10]
    #Heap_sort(arr)
    #print("정렬 후: ", end=' ')
    #print(arr)
    #print("heap sort", Heap_sort(arr))
main()
