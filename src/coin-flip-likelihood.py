def find_flip_likelyhood(flip_string,head_prob):
  probability = 1
  for result in flip_string:
    if result == "H":
      probability *= head_prob
    else:
      probability *= (1-head_prob)
  print(round(probability,5))

def find_flip_likelyhood_function(flip_string):
  head_count = 0
  for result in flip_string:
    if result == "H":
      head_count += 1
  print("L(p|"+flip_string+") = (p)^"+ str(head_count)+" * (1-p)^"+ str(len(flip_string)-head_count))

find_flip_likelyhood("HHTTH",0.5)

find_flip_likelyhood("HHTTH",.55)

find_flip_likelyhood_function("HHTTH")



