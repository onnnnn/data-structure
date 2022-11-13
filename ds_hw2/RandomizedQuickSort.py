# implementing 3 randomized quick sort
# Lomuto Partition, Hoare Partition, 3-Way Partition
from random import randint


def lomuto(arr, start, end):
    if start < end:
        pivotIndex = _lomuto_partition(arr, start, end)
        lomuto(arr, start, pivotIndex - 1)
        lomuto(arr, pivotIndex + 1, end)
    return arr

def _lomuto_partition(arr, start, end):
    n = len(arr)
    pivot = arr[end]
    nextIndex = start
    for i in range(start, n-1):
        if arr[i] < pivot:
            arr[nextIndex],arr[i] = arr[i],arr[nextIndex]
            nextIndex += 1
    arr[nextIndex],arr[end] = arr[end],arr[nextIndex]
    return nextIndex

def hoare(arr, start, end):
    if start < end:
        pivotIndex = _hoare_partition(arr, start, end)
        hoare(arr, start, pivotIndex-1)
        hoare(arr, pivotIndex+1, end)
    return arr

def _hoare_partition(arr, start, end):
    pivot = arr[start]
    leftPointer = start+1
    rightPointer = end
    done = False
    while not done:
        while leftPointer <= rightPointer and arr[leftPointer] <= pivot:
            leftPointer += 1
        while arr[rightPointer] >= pivot and rightPointer >=leftPointer:
            rightPointer -= 1
        if rightPointer < leftPointer:
            done= True
        else:
            arr[leftPointer],arr[rightPointer] = arr[rightPointer],arr[leftPointer]
    arr[start],arr[rightPointer] = arr[rightPointer],arr[start]
    return rightPointer

def _threeways_partition(arr: list, l, r):
    """
    partition3: A partition for quicksort algorithm. We'll use the 3-way to handle few equal elements in array (happens
    a lot in practical use.)
    This function is called from the main function quick_sort.
    """
    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = arr[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt



def three_ways(arr: list, l, r) -> list:
    """
    quick_sort: One of the most used sorting algorithm. 
    It makes to recursive calls. One to sort the left part separately, other for sorting the right part.
    The partition key is chosen randomly via ``random.randint(l, r)`` and it's between the ``l,  r``.
    
    PARAMETERS:
    -----------
    A: Array or the sequence that we want to sort.
    l: The lower bound of the array that we want to sort. It's not very important we might replace it by a wrapper function
    that only takes in an array as input. In this case it's the first element in the left part of the array.
    r: It's the same as l, only differs as it's the first element from the end.
    
    RETURNS:
    -------
    Sorted list A.
    """
    if l >= r: 
        return
    k = randint(l, r)
    arr[k], arr[l] = arr[l], arr[k]
    
    lt, gt = _threeways_partition(arr, l, r)
    three_ways(arr, l, lt - 1)
    three_ways(arr, gt + 1, r)
    return arr

if __name__ == "__main__":
    pass