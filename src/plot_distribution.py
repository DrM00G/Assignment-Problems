import matplotlib.pyplot as plt
from monte_carlo_probability import Monte_Carlo_Probability
from probobility import Probability
plt.style.use('bmh')
x_coords = [0,1,2,3,4,5,6,7,8,9,10]
probablility_results = [Probability(x,10) for x in x_coords]
plt.plot(x_coords,probablility_results,linewidth = 2.5)
for _ in range(5):
    plt.plot(x_coords,[Monte_Carlo_Probability(x,10) for x in x_coords],linewidth = 0.75)
plt.legend(['True','MC 1','MC 2','MC 3','MC 4','MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution and Monte Carlo Simulations: 10 Coin Flips')
plt.savefig('plot.png')
plt.show()