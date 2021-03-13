
graph={"A":["D","B"],"D":['C',"A","B"],'C':['D'],"B":["A","D"]}

def completion_check(paths):
  for path in paths:
    if len(path)<11:
      return False
  return True

paths=[["A"]]
while completion_check(paths)== False:
  split=paths[0]
  paths.remove(paths[0])
  for node in graph[split[len(split)-1]]:
    new_path=[node for node in split]
    new_path.append(node)
    paths.append(new_path)

print(len(paths))


