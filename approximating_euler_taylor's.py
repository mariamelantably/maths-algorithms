from math import e
errorThreshold = 10**(-15)
k = 0 #counter for k    
fact = 1 #(k+1)!
err = (e - (1/e)) #variable for current error
while abs(err) > errorThreshold:
    if k%2 == 0: #determines if k is even or odd
        err = (e - 1/e)/fact
    else:
        err = (e + 1/e)/fact
    k += 1
    fact *= (k+1)
if err > 0:
    sign = "Positive"
else:
    sign = "Negative" #no need to worry about err = 0, doesnt happen
print(f"Error = {err},  k = {k}, Sign = {sign}")