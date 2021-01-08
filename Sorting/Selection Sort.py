
def selection_sort(A):
    
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    print(A)

if __name__ == "__main__":
    A = [8, 3, 4, 9, 1, 2, 7, 6, 3, 4, 2, 5, 2, 9, 8, 5, 6, 7, 3, 4, 6, 5, 66, 5, 7, 0, 5, 8, 1, 4, 32, 5, 6, 4, 6, 8,5, 8, 3 ]
    # A = [2,3,1,5,0]

    selection_sort(A)