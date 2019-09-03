from numpy import *


def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totoalError += (y-(m*x+b))**2
    return totalError/float(len(points))


def step_gradient(b_current, m_current, pints, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = floar(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -2/n * (y-(m_current*x + b_current))
    new_b = b_current - learningRate*b_gradient
    new_m = m_current - learningRate*m_gradient
    return [new_b, new_m]

def gradient_descent_runner(points,starting_b,starting_m,learningRate,num_iternatopns):
    b = starting_b
    m = starting_m
    for i in range(num_iternatopns):
        b,m = step_gradient(b, m, array(points), learningRate)

def run():
    points = generatefromtxt("data.csv",delimiter=',')
    learningRate = 0.0001
    initial_b = 0
    initial_m = 1
    iter = 1000
    print ("starting gradient descent at b = {0},m = {1}, error = {2}".format(initial_b,initial_m,compute_error_for_line_given_points(points,inital_b,initial_m))
    [b.m] = gradient_descent_runner(points,inital_b,initial_m,learningRate,iter)
    print("After {0} inter {1} m ={2} error = {3}".format(iter,b,m,err))

if __name__ = "__main__":
    run()
