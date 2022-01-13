# Quick sort uses D&C method to reduce the size of problem 
# The base case is length of list is equal to 1 or 0 because for size of 1 and 0, we don't need to sort them
# every time we need to find a value and the values smaller than this pivot value will be combined to one list (list 1) and all values which are larger than the pivot will be combined to another list (list 2)
# apply quick sort for list 1 and list 2 (recursion)
# The method will stop when size of lists smaller than 2 



def quick_sort(arr):
    if len(arr) < 2:
        return arr 
    
    else:
        pivot = arr[0]
        less = [ele for ele in arr[1:] if ele <= pivot]
        large = [ele for ele in arr[1:] if ele > pivot]

        return quick_sort(less) + [pivot] + quick_sort(large)

if __name__ == '__main__':
    print(quick_sort([10, 5, 2, 3]))