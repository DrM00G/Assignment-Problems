arr1 = [[1,2,None],
        [None,3,None],
        [None,None,None]]
print(is_valid(arr1))
#True    (because no rows, columns, or diagonals are completely filled in) 

arr2 = [[1,2,None],
           [None,3,None],
           [None,None,4]] 
print(is_valid(arr2))
#False   (because a diagonal is filled in and it doesn't sum to 15)

arr3 = [[1,2,None],
           [None,3,None],
           [5,6,4]] 
print(is_valid(arr3))
#False   (because a diagonal is filled in and it doesn't sum to 15)

arr4 = [[None,None,None],
           [None,3,None],
           [5,6,4]] 
print(is_valid(arr4))
#True   (because there is one row that's filled in and it sums to 15)