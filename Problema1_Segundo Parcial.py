import math

def f(x):
    f = math.sin((1/x))
    return f


def simpson38(a,b):
    h = (b-a)/3
    x1 = a+h
    x2 = a+2*h
    integral = (3*h/8)*(f(a)+3*(f(x1)+f(x2))+f(b))
    return integral

def main():
    I = (simpson38(0.159154943, 2))
    print("Valor de la integración numérica por Simpson 3/8: \t",I)

main()