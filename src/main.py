from euler_estimator import EulerEstimator

euler = EulerEstimator(
                derivatives = [
                    (lambda t, x: -0.0003*x[1]*x[0]+0.01*x[1]+0.001),
                    (lambda t, x: -0.02*x[1]+0.0003*x[1]*x[0]),
                    (lambda t, x: 0.01*x[1])
                    ],
                point = (0,(1000,1,0))
            )
euler.plot([0,150], step_size = 0.001, filename = 'plot.png')