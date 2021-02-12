# def binary_search(entry, list): FORGOT THAT LIST WAS SUPPOSED TO BE SORTED
#   midpoint = len(list)//2
#   if list[midpoint] == entry:
#     return midpoint
  # else:
  #   if len(list) > 1:
  #     if len(list[:midpoint])>0:
  #       if binary_search(entry, list[:midpoint]) != None:
  #         return binary_search(entry, list[:midpoint])
  #     if len(list[midpoint+1:])>0:
  #       if binary_search(entry, list[midpoint+1:]) != None:
  #         return binary_search(entry, list[midpoint+1:])+len(list[:midpoint])+1
  #   else:
  #     return None

def binary_search(entry, sorted_list):
  midpoint = len(sorted_list)//2
  print(sorted_list[midpoint])
  if sorted_list[midpoint] == entry:
    return midpoint
  else:
    if len(sorted_list[:midpoint])>0 and entry < sorted_list[midpoint]:
        if binary_search(entry, sorted_list[:midpoint]) != None:
          return binary_search(entry, sorted_list[:midpoint])
    if len(sorted_list[midpoint+1:])>0 and entry > sorted_list[midpoint]:
        if binary_search(entry, sorted_list[midpoint+1:]) != None:
          return binary_search(entry, sorted_list[midpoint+1:])+len(sorted_list[:midpoint])+1
    else:
      return None

print("index: "+str(binary_search(34,[0,2,4,3,5,6,7,8,9,10,11,12,34,55])))
#34
print("index: "+str(binary_search(16, [1,2, 3,4, 5,6, 7, 8, 9, 10, 11,12, 13, 14, 15, 16])))
#3