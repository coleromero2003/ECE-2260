import math
def calculate_roots(coef):
    (a,b,c) = coef
    d = (b**2) - (4*a*c)
    if d < 0:
        d = -d
    sol1 = (-b-(math.sqrt(d)))/(2*a)
    sol2 = (-b-(math.sqrt(d)))/(2*a)
    return (sol1,sol2)
   
def compute_factorial(n):
    if n == 1:
        return n
    else:
        return n*compute_factorial(n-1)
    
def sum_factorial(n):
    sm = 0
    for i in range(n):
        sm = sm + compute_factorial(i+1)
    return sm
       
def left_riemann(delta_x, lb, ub):
    rng = ub - lb
    step = rng/delta_x
    estimate = 0
    for x in range (int(step)):
        
        estimate = estimate + (func(x*delta_x))*(delta_x)
    return estimate

def func(x):
    return ((math.e)**(-3*x))*(math.cos((math.pi)*x))
    
def right_riemann(delta_x, lb, ub):
    rng = ub - lb
    step = rng/delta_x
    estimate = 0
    for x in range (int(step)):
        
        estimate = estimate + (func((x+1)*delta_x))*(delta_x)
    return estimate
    
def midpoint_riemann(delta_x, lb, ub):
    rng = ub - lb
    step = rng/delta_x
    estimate = 0
    for x in range (int(step)):
        
        estimate = estimate + (func((x+.5)*delta_x))*(delta_x)
    return estimate
    
def trap_riemann(delta_x, lb, ub):
    rng = ub - lb
    step = rng/delta_x
    estimate = 0
    for x in range (int(step)):
        left = (func((x)*delta_x))*(delta_x)
        right = (func((x+1)*delta_x))*(delta_x)
        difference = left - right
        if difference < 0:
            difference = -difference
        if left > right:
            estimate = estimate + right + (difference/2)
        else:
            estimate = estimate + left + (difference/2)
    return estimate

def main():
    ##############################################################
    # Part 1
    ##############################################################
    print("Part 1 Results")
    
    coef = [2, 4, 0]
    roots = calculate_roots(coef)
    print("roots 1:")
    print(roots)
    coef = [1, 4, 4]
    roots = calculate_roots(coef)
    print("roots 2:")
    print(roots)
    
    coef = [1, 0, 9]
    roots = calculate_roots(coef)
    print("roots 3:")
    print(roots)
    coef = [2, 8, 26]
    roots = calculate_roots(coef)
    print("roots 4:")
    print(roots)
    
    ##############################################################
    # Part 2
    ##############################################################
    print("\n")
    print("Part 2 Results")
    
    for n in [4, 10, 16]:
        output_factorial = compute_factorial(n)
        print("computed factorial for n=%i is: %i" %
              (n, output_factorial))
    
    ##############################################################
    # Part 3
    ##############################################################
    print("\n")
    print("Part 3 Results")
    
    for n in [3, 5, 6]:
        output_summation = sum_factorial(n)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
        
    ##############################################################
    # Part 4
    ##############################################################
    print("\n")
    print("Part 4 Results")
    
    lb = 0
    ub = 10
    
    print("calculating left Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = left_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))
    print("calculating right Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = right_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))
    print("calculating midpoint Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = midpoint_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))
        
    print("calculating trapezoid Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = trap_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))
    
if __name__ == "__main__":
    main()