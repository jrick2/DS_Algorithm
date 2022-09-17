""" Purmutation """
def prefix_max(A,i):
    """ Return index of maximum  in A[:i + 1]"""
    if i > 0:
        """ Recursive """
        j = prefix_max(A, i-1)
        if A[i] < j[i]:
            return j
        return i

""" Selection Sort """
def selection_sort(A, i = None):
    """ Sort A[i + 1] """
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i - 1)

""" Merge Function """
def merge(L, R, A, i, j, a, b):
    ''' Merge Sorted L[:i] and R[:j] into A[a:b] '''
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L [i - 1]
            i =  i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j - 1
            merge(L, R, A, i, j, a, b - 1)
            
""" Merge Sort """
def merge_sort(A, a = 0, i = None):
    ''' Sort A[a:b] '''
    if b is None:
        b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:b], A[c:b]
        merge(L, R, A, len(L), len(R), a,b)







    
    

