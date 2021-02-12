def quicksort_without_swaps(data_list):
  if len(data_list) > 1:
    greater_than = []
    less_than = []
    split_value = data_list[len(data_list)-1]
    for n in range(len(data_list)-1):
      if split_value < data_list[n]:
        greater_than.append(data_list[n])
      else:
        less_than.append(data_list[n])
    result = quicksort_without_swaps(less_than)
    result.append(split_value)
    for n in quicksort_without_swaps(greater_than):
      result.append(n)
    return result
  else:
    return data_list

print(quicksort_without_swaps([1,5,3,10,7,5,8]))