import matplotlib.pyplot as plt #library used to create plots
import math #typical math library

actual_value = 0.4*math.sqrt(32) #actual value of the integral 

def f(x: int):
    return x*math.sqrt(x) #computes x^(3/2)

def simpsons_rule(f, n, a, b):
    #input: a function f (must be from float to float), the number of strips n, the start-point a and end-point b of the approximation
    #output: a number representing the simspons rule approximation of the integral from a to b
    current_coefficient = 4 
    s = f(a)
    step = (b-a)/n 
    current = a 
    for _ in range(1,n):
        current += step
        s += current_coefficient*f(current)
        current_coefficient = 6 - current_coefficient
    s += f(b)
    return ((b-a)*s)/(3*n) 

pow = 2
pows = []
errs = []
for i in range(24):
    error = simpsons_rule(f, pow, 0, 2) - actual_value
    pows.append(i+1)
    errs.append(math.log2(abs(error)))
    pow *= 2

ys = [(-2.5-4*x) for x in pows]
fig, ax = plt.subplots()
plt.plot(pows, errs, label = "Calculated error")
plt.plot(pows,ys, label = "Expected error")
ax.set(title = "Error for Simpson's Rule", xlabel = "Log of number of strips", ylabel = "Log of error ")
ax.legend()
ax.grid(True, which = 'both')
plt.show()