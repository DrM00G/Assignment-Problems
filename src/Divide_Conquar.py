def divide_and_conquer_sort(input_list):
  if len(input_list) > 1:
    # print("Input length "+str(len(input_list)))
    result = []
    # print("result: "+str(result))
    for n in range(len(input_list[:(len(input_list)//2)])):
      # print(str(n)+' '+str(input_list[:(len(input_list)//2)]))
      result.append(divide_and_conquer_sort(input_list[:(len(input_list)//2)])[n])
    for n in range(len(input_list[:(len(input_list)//2)])):
      inserted = 0
      for i in range(len(result)):
        if divide_and_conquer_sort(input_list[(len(input_list)//2):])[n] < result[i] and inserted == 0:
          new_result= []
          for j in result[0:i]:
            new_result.append(j)
          new_result.append(divide_and_conquer_sort(input_list[(len(input_list)//2):])[n])
          for j in result[i:len(result)]:
            new_result.append(j)    
          inserted = 1
          result=new_result
      if inserted == 0:
        result.append(divide_and_conquer_sort(input_list[(len(input_list)//2):])[n])
    # print("Result: "+str(result))
    return(result)
  else:
    # print("Single: "+str(input_list))
    return(input_list)

