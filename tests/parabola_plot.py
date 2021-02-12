
import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

print("Now graph")
euler_graph = EulerEstimator(derivative = (lambda x: x+1), point = (1,4))
euler_graph.plot([-5,5], step_size = 0.1, filename = 'plot.png')
