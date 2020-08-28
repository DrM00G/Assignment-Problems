from probobility import Probability
import math

flips = {
    'Justin': ['THTT',  'HTHT',  'TTTH',  'THHT',  'HTHH',  'TTTH',  'THTH',  'HHTH',  'TTTT',  'HTTH',  'HHTT',  'THHH',  'HHHH',  'THTH',  'HTTH',  'TTHH',  'HTHT',  'HHHT',  'THHT',  'TTTH'],
    'George': ['THTH', 'HTHT',  'THTH',  'HHTH',  'THTH',  'TTHT',  'THTH',  'TTTH',  'THTH',  'TTHT',  'THHT',  'HTTH',  'THTH',  'THHT',  'THHT',  'THTH',  'THTH',  'THHT',  'THTH',  'THTH'],
    'David': ['TTHH',  'HHTT',  'HHTT',  'TTHH',  'HTHT',  'THTH',  'THTH',  'THTH',  'HTHT',  'HTHT',  'THTH',  'HTHT',  'THHH',  'THTH',  'HHTT',  'HHTT',  'TTTH',  'HHTH',  'HTHH',  'TTTH'],
    'Elijah': ['THTT', 'HTHT', 'HTHH', 'HHHT', 'TTHH', 'THHH', 'TTTT', 'HHTT', 'TTTH', 'TTHH', 'HTHT', 'HTHT', 'TTTT', 'HTTT', 'TTTH', 'HTTT', 'TTHH', 'THTH', 'THHH', 'HTHH'], 
    'Colby': ['HTTH',  'HTHH',  'THTT',  'HHTH',  'TTHT',  'HTTT',  'THHH',  'TTHH',  'HHTT',  'THTH',  'HHTT',  'THTH',  'THHH',  'TTHH',  'THTT',  'HHTH',  'HTTH',  'HTHH',  'TTHT',  'HTTT']
}

real_probablity = [Probability(x,4) for x in range(5)]
results = {}

def analyze_coinset(head_nums,flip_results):
    succesful_results_num = 0
    for coindata in flip_results:
        heads = 0
        for outcome in coindata:
            if outcome == 'H':
                heads+=1
        if heads == head_nums:
            succesful_results_num+=1
    return succesful_results_num/len(flip_results)


for human in flips:
  results[human]=[]
  for n in range(5):
    results[human].append(analyze_coinset(n,flips[human]))

def kl_divergence(real_prob,found_prob):
    divergence = 0
    for n in range(len(found_prob)):
        if found_prob[n] != 0:
            divergence += found_prob[n]*(math.log(found_prob[n]/real_prob[n]))
    return divergence

for human_result in results:
  print(human_result+" results:")
  print(flips[human_result])
  print("Kl Divergence: "+str(kl_divergence(real_probablity,results[human_result])))
  print("-------------------------")



