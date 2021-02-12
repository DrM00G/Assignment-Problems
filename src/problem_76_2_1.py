import random

def random_draw(distribution):
  cuml_distr=[distribution[0]]
  for n in range(len(distribution)-1):
    cuml_distr.append(cuml_distr[n]+distribution[n+1])
  rand = random.uniform(0,1)
  for n in range(len(cuml_distr)):
    if rand<=cuml_distr[n]:
      return n 
      break

distrib={"0":0,"1":0}
for n in range(1000):
  rand=random_draw([0.5,0.5])
  distrib[str(rand)]=distrib[str(rand)]+1
for n in distrib:
  distrib[n]=distrib[n]/1000
print("expected:"+str([0.5,0.5]))
print("result"+str(distrib))

print()

distrib={"0":0,"1":0,"2":0}
for n in range(1000):
  rand=random_draw([0.25, 0.25, 0.5])
  distrib[str(rand)]=distrib[str(rand)]+1
for n in distrib:
  distrib[n]=distrib[n]/1000
print("expected:"+str([0.25, 0.25, 0.5]))
print("result"+str(distrib))

print()

distrib={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0}
for n in range(1000):
  rand=random_draw([0.05, 0.2, 0.15, 0.3, 0.1, 0.2])
  distrib[str(rand)]=distrib[str(rand)]+1
for n in distrib:
  distrib[n]=distrib[n]/1000
print("expected:"+str([0.05, 0.2, 0.15, 0.3, 0.1, 0.2]))
print("result"+str(distrib))

print()