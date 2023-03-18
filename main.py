import numpy as np                                  # Helps us with defining the problem, i.e sin(x)
import matplotlib.pyplot as plt                     # Can Visualise the Probelm
import random                                       # helps with generating random variables
 
def equation(x):                                    # the function we want to integrate is defined here, you can change this to any function you want to integrate
    return np.sin(x)    
    
x_ = np.linspace(0,np.pi,101)                        # not needed for the problem, but helps to show you the function before doing Monte Carlo
plt.plot(x_,equation(x_))                             # this will plot the function we want to integrate

under_curve = 0                                     # Initially there are 0 points under the curve, we will add to this with each iteration
upper_limit = np.pi                                 # You can change this to suit your upper bound of your integral
lower_limit = 0                                     # Lower bound
points = 2000                                       # How many points we want to generate, more points, more accurate

for i in range(points):                             # For loop to simulate x, and y
    x = random.uniform(0,upper_limit)               #generate x between 0 and upper limit
    y = random.uniform(0,1)                         # generate y between 0 and 1, remember if you want to use your own function, this may need to be changed
    
    if y <= equation(x):                            # check if the point is below the curve
        under_curve = under_curve + 1               # add point to under_curve
        plt.scatter(x,y,color='b')                  # scatter plot the x,y, color is blue
    else:                                           # incase it's not under the curve
        plt.scatter(x,y,color='r')                  # plot x,y and color it red
plt.plot(x_,equation(x_),color='g',linewidth=3)     # not needed but good to see it compared to the actual function

estimate_integral = (under_curve/points) * (upper_limit - lower_limit) #count the points under curve, divide by total curve, multiple by your upper bound - lower bound
print(estimate_integral)                                               #print the estimate


