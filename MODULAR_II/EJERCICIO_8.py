'''
8. Design a method called solveSecondOrderEquation that receives three integer
positive numbers corresponding to the coefficients of a second order equation
(ax2+bx+c=0) and computes its possible solutions. If the parameters are not valid the
method should return None.
'''

def solveSecondOrderEquation(ax, bx, c):

while 1>0:
    a=int(input("Indique un número positivo "))
    b=int(input("Indique un número positivo "))
    c=int(input("Indique un número positivo "))
    
    if a <= 0 or b <= 0 or c < 0:
        mensaje = None
        
    else:
        mensaje = solveSecondOrderEquation(ax, bx, c)
    
    print(mensaje)