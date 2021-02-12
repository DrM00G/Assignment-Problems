import matplotlib.pyplot as plt

class EulerEstimator:
  def __init__(self, derivatives, point):
    self.derivatives = derivatives
    self.point = point

  def calc_derivative_at_point(self):
        derivatives = {}
        for equasion in self.derivatives:
            derivatives[equasion]=(self.derivatives[equasion](self.point[0],self.point[1]))
        return derivatives

  def step_forward(self, step):
    d_a_p = self.calc_derivative_at_point()
    new_points={}
    for delta in d_a_p:
      new_points[delta]=self.point[1][delta]+(step*d_a_p[delta])
    self.point = (self.point[0]+step,new_points)

  def go_to_input(self, target_value, step_size):
    while abs(self.point[0]-target_value) > abs(step_size):
      self.step_forward(step_size)
    self.step_forward(target_value-self.point[0])
    
  
  def plot(self, interval, step_size = 0.1, filename = 'plot.png'):
        # print(self.point)
        self.go_to_input(interval[0], 0.1)
        # print(self.point)
        coords = [[],{x:[]for x in self.point[1]}]
        while abs(self.point[0]-interval[1]) > abs(step_size):
          self.step_forward(step_size)
          coords[0].append(self.point[0])
          for coord in coords[1]:
            coords[1][coord].append(self.point[1][coord])
        self.step_forward(interval[1]-self.point[0])
        coords[0].append(self.point[0])
        for coord in coords[1]:
          coords[1][coord].append(self.point[1][coord])
        plt.style.use('bmh')
        for coord in coords[1]:
          plt.plot(coords[0],coords[1][coord],linewidth = 2.5)
        plt.title("Plot of Euler Estimator")
        plt.savefig(filename)
        plt.show()