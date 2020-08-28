import random
def Monte_Carlo_Probability(num_heads, num_flips,range_trials= 1000):
  succses_num_heads = 0
  for _ in range(range_trials):
      rand_result = []
      for _ in range(num_flips):
          rand_result.append(random.choice([1,2]))#1 heads, 2 tails
      head_count = 0
      for elem in rand_result:
          if elem == 1:
              head_count+=1
      if head_count == num_heads:
          succses_num_heads = succses_num_heads + 1
  return succses_num_heads/range_trials
