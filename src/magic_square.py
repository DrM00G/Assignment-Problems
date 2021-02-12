def is_valid(arr):
  Possible = True
  for row in range(len(arr)):
    
    if None not in arr[row]:
      if sum(arr[row]) != 15 or arr[row][0]==arr[row][1] or arr[row][0]==arr[row][2] or arr[row][2]==arr[row][1]:
        Possible = False
        break
    test_list = [arr[0][row],arr[1][row],arr[2][row]]
    if None not in test_list:
      if sum(test_list) != 15 or test_list[0]==test_list[1] or test_list[0]==test_list[2] or test_list[2]==test_list[1]:
        Possible = False
        break
  if Possible:
    for row in [[0,1,2],[2,1,0]]:
      test_list = [arr[row[0]][0],arr[row[1]][1],arr[row[2]][2]]
      if None not in test_list:
        if sum(test_list) != 15 or test_list[0]==test_list[1] or test_list[0]==test_list[2] or test_list[2]==test_list[1]:          
          Possible = False
          break
  return(Possible)
  
def find_arrays():
  possible_rows = []
  possible_arrs = []
  for x in range(9):
    for y in range(9):
      for z in range(9):
        row = [x+1,y+1,z+1]
        if sum(row) == 15 and row[0]!=row[1] and row[0]!=row[2] and row[2]!=row[1] and row not in possible_rows:
          possible_rows.append(row)
  for x in possible_rows:
    for y in possible_rows:
      for z in possible_rows:
        if is_valid([x,y,z]) and [x,y,z] not in possible_arrs:
          possible_arrs.append([x,y,z])
          print([x,y,z])
          print("--------")

















    
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

find_arrays()