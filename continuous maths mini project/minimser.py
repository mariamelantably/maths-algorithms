import numpy as np
from math import exp

X = np.loadtxt("cm-sheet5-X.txt")
y = np.loadtxt("cm-sheet5-y.txt")

#function to compute the loss function for a given weight
def loss(w):
    global X, y
    s = 0
    for i in range(2000):
        z = np.dot(X[i], w)*(-1*y[i]) 
        s += exp(z)
    return s

#function to compute the gradient of the loss function for a given weight
def gradOfLoss(w):
    global X, y
    s = np.zeros(shape = 137)
    for i in range(2000):
        s += exp(np.dot(X[i], w)*-1*y[i])*(-1*y[i])*X[i]
    return s

def gradientDescent(f, df , x , alph0, rho , sigm = 10**(-4), N = 5000, tol = 10**(-8)):
    g = df(x) #g stores current gradient
    g0 = g
    d = -1*g #d stores current -1*g
    fn = f(x) #fn stores value of f(xn-1)
    alph = alph0 #stores current step length
    n = 0
    while True:
        alphOld = alph #alphOld is prev. step length
        xnew = x + alph*d #stores new value of x
        fnew = f(xnew) #stores new value of step length
        #armijo rule to backtrack steplength
        while (fnew >= fn + sigm*alph*np.dot(g, d)):
            alph = rho*alph
            xnew = x + alph*d
            fnew = f(xnew)
        n += 1
        fn = fnew
        x = xnew 
        gOld = g
        g = df(xnew)
        dOld = d
        d = -1*g
        alph = (alphOld*(np.dot(gOld, dOld)))/(np.dot(g, d))
        if (n == N) or np.linalg.norm(g - gOld) < tol*(1 + np.linalg.norm(g)):
            break #break out if our conditions are met
    return xnew

#signum function
def sgn(t):
    if t >= 0: return 1 
    else: return -1

x0 = 1/5700*np.ones(shape = 137) #starting x0
w = gradientDescent(loss, gradOfLoss, x0, 0.00001, 0.5)
x = 0
#find the number of vectors where the w managed to seperate the data
for i in range(2000):
    if sgn(np.dot(w, X[i])) == y[i]:
        x += 1
print(f"Number of vectors where signum matched yi: {x}")
print(f"Loss function: {loss(w)}")

