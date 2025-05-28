def f(x):
    return x**2

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x_val = 2
print("f(x) =", f(x_val))
print("Approximate derivative at x =", x_val, "is", derivative(f, x_val))
