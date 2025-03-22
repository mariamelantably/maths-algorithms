from math import exp #this function returns e^x
import matplotlib.pyplot as plt #library for generating graphs
from tabulate import tabulate #library for tabulation

def newtons_method(lamba : float):
    x = 0 #set x_0 = 0, as f(0) > 0
    tol = 4*(10**-16) #set tolerance to be 4*𝜖
    while True: 
        old_x = x #store x(n-1) for breaking out of the loop
        er = exp(lamba*(x - 1)) 
        x = x - (er - x)/(lamba*er - 1) #newtons method iteration
        if abs(x - old_x) < tol*(1 + abs(x)): #last iteration didnt change significantly, both absolute & relative error
            break
    return x #computed extinction probability

lambdas = [] #stores poisson parameters
probs = []
for i in range(1, 57): #computes extinction probability for 1.125 to 8 in steps of 0.125
    lambd = 1 + i*0.125 
    lambdas.append(lambd)
    probs.append(newtons_method(lambd))


pairs = list(zip(lambdas, probs))
table = tabulate(pairs, headers = ["λ", "extinction probability"], tablefmt= "pretty", numalign="right" )
print(table)

fig, ax = plt.subplots()
plt.plot(lambdas, probs)
ax.set(title = "Variation of extinction probability with poisson parameter, λ", xlabel = "λ (Poisson Parameter)", ylabel = "Probability of extinction")
ax.grid(True, which = 'both')
plt.show()
    