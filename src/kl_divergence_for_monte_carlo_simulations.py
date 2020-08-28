import sys
sys.path.append('src')
from monte_carlo_probability import Monte_Carlo_Probability
from probobility import Probability

import math

def kl_divergence(p,q):
    return sum([p[i]*(math.log(p[i]/q[i])) for i in range(len(p))])
def non_zeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 0.0001
    return nums

p = [0.2, 0.7, 0.1]
q = [0.1, 0.8, 0.1]
assert round(kl_divergence(p,q),11) == 0.04515746127, ('KL divergence does not work should be',0.04515746127,'got',round(kl_divergence(p,q),11))


real_results = non_zeros([Probability(x, 5) for x in range(5)])
monte_carlo_100 = non_zeros([ Monte_Carlo_Probability(x, 5,range_trials=100) for x in range(5)])
monte_carlo_1000 = non_zeros([ Monte_Carlo_Probability(x, 5,range_trials=1000) for x in range(5)])
monte_carlo_10000 = non_zeros([ Monte_Carlo_Probability(x, 5,range_trials=10000) for x in range(5)])

print("Divergence with 100 trials: ")
print(kl_divergence(real_results, monte_carlo_100))
print("------------------------------")
print("Divergence with 1000 trials: ")
print(kl_divergence(real_results, monte_carlo_1000))
print("------------------------------")
print("Divergence with 10000 trials: ")
print(kl_divergence(real_results, monte_carlo_10000))

