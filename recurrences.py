import matplotlib.pyplot as plt #library used to create plots
from tabulate import tabulate
from math import log10 as lg #use log 10 to make it easier to see the recurrence

xs = [1/3, 1/12] #array to store the values
count = 2 #stores currently computed numbers - avoids invokations of length 
while count < 100: 
    xs.append(9/4 * xs[-1] - 1/2*xs[-2]) #compute new value
    count += 1
indices = [lg(i) for i in range(1, 101)] #store indices in array
pows = [lg(3/4*((1/4)**k)) for k in range(1, 101)]
xsLogged = [lg(j) for j in xs] #take logs

pairs = list(zip(indices, xs)) #pair each x with its corresponding index
table = tabulate(pairs, headers = ["i", "Xi"], tablefmt= "pretty", numalign="right" )
print(table)

fig, ax = plt.subplots()
fig, ax = plt.subplots()
plt.plot(indices, xsLogged, label = "Computed Recurrence")
plt.plot(indices, pows, label = "Expected Recurrence")
ax.set(title = "Computing Recurrences", xlabel = "i", ylabel = "Xi")
ax.legend()
ax.grid(True, which = 'both')
plt.show()



