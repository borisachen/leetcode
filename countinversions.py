"""
# inversion
[1, 2, 3] => 0
[2, 1, 3] => 1
[1, 3, 2] => 1

[3, 2, 1] => ? 1? 2?
(3,2) 
(2,1)
(3,1) ==> 3
return the count of # inversions
        |
[ 1 9 3 5 4 6 7 ]
[ o x o o x o o ] 


[ 1 9 | 3 5 | 4 6 | 7 8]
   0     0
[ 1 9 | 3 5 ]
  1 vs 35:0
  9 vs 35:2
  _________: 2
  # 
  

"""

def say_hello():
    print 'Hello, World'
    
def count_inversions(a):
    # strategy: merge sort like; 
    if len(a)==1:
        return 0
    elif len(a)==2:
        if a[0] <= a[1]:
            return 0
        else:
            return 1
    elif:
        mid = len(a)/2
        current_layer = 0
        for i in range(0,mid):
            j = mid+1
            while j < len(a):
                if a[i] <= a[j]:
                    break
                else:
                    current_layer += 1
                j += 1
            
        c = current_layer + count_inversions(a[0:mid]) + count_inversions(a[mid+1:])
        sorted_left = a[0:mid].sort()
        sorted_right = a[mid+1:].sort()
        sorted_a = a.sort()
        return c, sort_a
        


def mergesort_inversion(x):
    if len(x)==0 or len(x)==1:
        return x, 0
    else:
        mid = len(x)/2
        a, a_count = mergesort_inversion(x[:mid])
        b, b_count = mergesort_inversion(x[mid:])
        mergedlist, merge_count = merge_inv(a,b)
        total_inv = a_count + b_count + merge_count
        return mergedlist, total_inv

def merge_inv(a,b):
    res = []
    count = 0
    while len(a)>0 and len(b)>0:
        if a[0] > b[0]:
            res += [b[0]]
            b = b[1:]
            # if a[0]>b[0], then the remaining elements in A are inversions 
            count += len(a)
        else:
            res += [a[0]]
            a = a[1:]
    if len(a) > 0:
        res += a
    if len(b) > 0:
        res += b
    return res, count

mergesort_inversion([1, 20, 6, 4, 5])

mergesort_inversion([5,7,3,4,7,3,4,7,3,42,5])
mergesort_inversion([3,1])
mergesort_inversion([3,2,1])


"""
Basic merge sort:        
 """        
def mergesort(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        mid = len(x)/2
        a = mergesort(x[:mid])
        b = mergesort(x[mid:])
        return merge(a,b)

def merge(a,b):
    res = []
    while len(a)>0 and len(b)>0:
        if a[0] < b[0]:
            res += [a[0]]
            a = a[1:]
        else:
            res += [b[0]]
            b = b[1:]
    if len(a) > 0:
        res += a
    if len(b) > 0:
        res += b
    return res

merge([1,3,5,7],[2,4,6,8])

mergesort([5,7,3,4,7,3,4,7,3,42,5])


