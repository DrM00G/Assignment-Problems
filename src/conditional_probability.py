flips = {
    'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
    'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
    'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
    'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
    'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
}

def find_probobility(test,dataset):
  succsesful_tests = 0
  possible_tests = 0
  # print(test)
  for h_or_t in range(len(dataset)-1):
    # print(dataset[h_or_t]+""+dataset[h_or_t+1])
    if dataset[h_or_t]==test[1]:
      possible_tests = possible_tests + 1
      if dataset[h_or_t+1]==test[0]:
        succsesful_tests = succsesful_tests + 1
  return str(succsesful_tests)+"/"+str(possible_tests)


tests = ["HH","TH","HT","TT"]
for human in flips:
  print("==============")
  print("Testing "+human)
  print("==============")
  dataset_quads = flips[human].split(' ')
  dataset = []
  for quad in dataset_quads:
    for data in quad:
      dataset.append(data)
  print(len(dataset))
  for test in tests:
    print(test+" Probobility")
    print(find_probobility(test,dataset))
    print("-------------")

print()
print()
test_flips="HHTTHT"
print("==============")
print("Testing basic flips")
print("==============")
for test in tests:
  print(test+" Probobility")
  print(find_probobility(test,test_flips))
  print("-------------")