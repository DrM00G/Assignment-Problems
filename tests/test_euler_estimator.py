import sys
sys.path.append('src')
from euler_estimator import EulerEstimator
# euler = EulerEstimator(derivative = (lambda x: x+1),point = (1,4))
# #                         

# print(euler.point)
# #(1,4)
# print(euler.calc_derivative_at_point())
# #2     (because the derivative is f'(x)=x+1, so f'(1)=2)

# euler.step_forward(0.1)
# euler.point
# # (1.1, 4.2)        (because 4 + 0.1*2 = 4.2)

# print(euler.calc_derivative_at_point())
# #2.1

# euler.step_forward(-0.5)
# print(euler.point)
# #(0.6, 3.15)        (because 4.2 + -0.5*2.1 = 3.15)

# euler.go_to_input(3, step_size = 0.5)

# # note: you should move to the x-coordinate of 3
# #       using a step_size of 0.5, until the final step,
# #       in which you need to reduce the step_size to hit 3

# # the following is provided to help you debug:

# # point, derivative, deltas
# # (0.6, 3.15), 1.6, (0.5, 0.8)
# # (1.1, 3.95), 2.1, (0.5, 1.05)
# # (1.6, 5), 2.6, (0.5, 1.3)
# # (2.1, 6.3), 3.1, (0.5, 1.55)
# # (2.6, 7.85), 3.6, (0.4, 1.44)

# print(euler.point)
# # (3, 9.29)

euler = EulerEstimator(
                derivatives = {
                "suseptible":(lambda t, x: -0.001*x["suseptible"]*x["infected"]),
                "infected":(lambda t, x: 0.001*x["suseptible"]*x["infected"]-0.05*x["infected"]),
                "recovered":(lambda t, x: 0.05*x["infected"])
                },
                point = (0,{"suseptible":500,"infected":5,"recovered":0})
            )
print("Derivitive: "+str(euler.calc_derivative_at_point()))

# print("Point: "+str(euler.point))
# #(0, (0, 0, 0))
# print("Derivitive: "+str(euler.calc_derivative_at_point()))
# #[1, 0, 0]

# euler.step_forward(0.1)
# print("Point: "+str(euler.point))

# print("Derivitive: "+str(euler.calc_derivative_at_point()))
# [1.1, 0.1, 0]
# euler.step_forward(-0.5)
# print("Point: "+str(euler.point))
# (-0.4, (-0.45, -0.05, 0))

# euler.go_to_input(5, step_size = 2)
# print(euler.point)
# (5, (10.88, 1.09, -9.58))
euler.plot([0,50],0.1)