def searchInsert(A, target):
    insertPos = 0
    for index, elem in enumerate(A):
        if elem == target:
            return index
        elif elem > target:
            return index
    return len(A)

if __name__ == '__main__':
    print searchInsert([1,3,5,6], 5)
    print searchInsert([1,3,5,6], 2)
    print searchInsert([1,3,5,6], 7)
    print searchInsert([1,3,5,6], 0)
