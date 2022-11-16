def f(x,y):
    result = (x**2)+(y**2)
    return result

def rungekutta(x0, y0, xf, h): 
    x = x0
    y = y0
    while x <= xf:
        k1 = h*f(x, y)
        k2 = h*f(x+(h/2), y+(k1/2))
        k3 = h*f(x+(h/2), y+(k2/2))
        k4 = h*f(x+h, y+k3)
        
        k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y = y + k
        x = x + h

    return y

rk = (rungekutta(0, 1, 0.8, 0.01))
#print(rk)

print("x: 0.80")
print("y(0.80): ", rk)

