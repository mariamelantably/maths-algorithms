import numpy as np
import math

#given x and y, computes f(x,y) and returns answer as a numpy array
def f(x : float, y : float): 
    x0 = 1/((2-x)*(2-y)) - x
    y0 = 2/((3-2*x)*(3-y)) - y
    return np.array([x0, y0])

#given x and y, computes the jacobian at (x,y) and returns answer as a numpy array
def jacobian(x : float, y : float):
    x0 = 1/(((2-x)**2)*(2-y)) - 1
    x1 = 1/((2-x)*((2-y)**2))
    y0 = 4/(((3-2*x)**2)*(3-y))
    y1 = 2/(((3-y)**2)*(3-2*x)) - 1
    return np.array([[x0, x1], [y0, y1]])

#computes the vector-norm of a 2-dimensional vector
def norm(x, y):
    return math.sqrt(x**2 + y**2)

x = 0 #start with (0,0)
y = 0
tol = 4*(10**-16) #set tolerance to be 4*𝜖
while True:
    delta = np.linalg.solve(jacobian(x, y), -1*f(x, y)) #solve for Δx : (J(f)(x,y))Δx = -f(x,y)
    x = x + delta[0] #increment x
    y = y + delta[1] #increment y
    if norm(delta[0], delta[1]) < tol*(1 + norm(x, y)):
        break
print(f"Extinction probability for type A: {x} \nExtinction probability for type B: {y}")



