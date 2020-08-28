import sys
sys.path.append('src')
from probobility import Probability
sys.path.append('src')
from monte_carlo_probability import Monte_Carlo_Probability

print("Probobility: "+str(Probability(5,8)))
print("Monte Carlo Probability:")
for n in range(3):
  print(Monte_Carlo_Probability(5,8))
