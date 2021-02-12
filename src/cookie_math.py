cookie_stats = ['ID', 'Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]

data = [[ 1 , 'Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
[ 2  , 'Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
[ 3  , 'Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
[ 4  , 'Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
[ 5  , 'Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
[ 6  , 'Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
[ 7  , 'Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
[ 8  , 'Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
[ 9  , 'Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
[ 10 , 'Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
[ 11 , 'Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
[ 12 , 'Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
[ 13 , 'Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]]

def compare_cookies(cookie,data_cookie):#data cookie is the cookie we already know the clasification of
  compared_stats = [(cookie[n]-data_cookie[n+2])**2 for n in range(len(data_cookie)-2)]
  return(sum(compared_stats)**(1/2))

def sort_closest_cookie(cookie_data):
  highest_rated = cookie_data[0]
  for cookie in cookie_data:
    if cookie[2] > highest_rated[2]:
      highest_rated = cookie
  return (cookie_data.index(highest_rated))


def closest_cookie(cookie,cookie_data):
  close_list = []
  sorted_list = []
  for data_cookie in cookie_data:
    close_list.append([data_cookie[0],data_cookie[1],compare_cookies(cookie,data_cookie)])
  for n in range(len(cookie_data)):
    sorted_list.append(close_list.pop(sort_closest_cookie(close_list)))
  return(sorted_list[::-1])

def cagagory_average(cookie_data):
  catagories=['Shortbread',[0],'Sugar',[0],'Fortune',[0]]
  for cookie in cookie_data:
    catagories[catagories.index(cookie[1])+1].append(cookie[2])
  # print(range(len(catagories)//2))
  for n in range(len(catagories)//2):
    print(catagories[(n)*2]+": "+str(sum(catagories[(n)*2+1])/len(catagories[(n)*2+1])))

test_cookie=[0.10, 0.15 , 0.30 , 0.45]

# print(closest_cookie(test_cookie,data))

cagagory_average(closest_cookie(test_cookie,data))

  

