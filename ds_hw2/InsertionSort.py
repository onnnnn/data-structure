# https://www.geeksforgeeks.org/python-program-for-insertion-sort/

def insertion_sort(arr: list):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr


if __name__ == "__main__":
    arr = [4, 7, 3, 8, 9, 5]
    print("original list:", arr)
    arr_sorted = insertion_sort(arr)
    print("sorted list:", arr_sorted)