results = []
for a in range(6):
  for b in range(6):
    results.append((a+1)-(b+1))

print(results)

result = [[],[],[],[],[],[],[],[],[],[],[]]
for a in range(6):
  for b in range(6):
    result[((a+1)-(b+1))+5].append(1)


for n in range(len(result)):
  print(str(n-5)+","+str(sum(result[n])))