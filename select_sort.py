# select sort means, every iteration, select the largest value in the list and put it in the new list
# finding the largest value O(n) and repeat n times == O(n^2)

def findsmallest(arr):
    smallest = arr[0]
    smallest_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    return smallest_idx


def selectionSort(arr):
    newArray = []

    for i in range(len(arr)):
        smallest_idx = findsmallest(arr)
        newArray.append(arr.pop(smallest_idx))

    return newArray

if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))


