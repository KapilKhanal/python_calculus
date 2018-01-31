# -*- coding: utf-8 -*-

"""Main module."""
def derivative(f, h):
    '''Returns a new function that is the approximation of
    the derivative of f with respect to h.'''

    return lambda x: (f(x+h) - f(x)) / h #returns a function
def square(x):
    return x**4
def kth_derivative(f,h,k):
    """Returns a kth derivative of the function as required"""
    if k ==1:
        return derivative(f,h)
    else:
        return derivative(kth_derivative(f,h,k-1),h)


def integrate_function(f,n,x_low,x_high):
    nrectangles = n # number of x-values to use to calculate the average.

    #Integration domain
    xlow = x_low
    xhigh = x_high

    #Integrand


    xvalues = np.linspace(xlow, xhigh, nrectangles)
    fvalues = f(xvalues) # f(x_i) for each rectangle
    areas = fvalues * (xhigh - xlow)/nrectangles # A_i for each rectangle
    integral = sum(areas)
    plt.plot(xvalues,fvalues)
    

    plt.show()
    return integral

