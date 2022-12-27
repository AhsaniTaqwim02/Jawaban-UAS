def Trapezoid(a,b,f):
    n = 100
    def trapezoid(f,a,b,n=10):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))


for i in range(0,1):
    Trapezoid(i+2,i+4,lambda x: 2*x**1 + 1)
    
for i in range(0,1):
    Trapezoid(i+3,i+5,lambda x: 2*x**1 + 2)


for i in range(0,1):
    Trapezoid(i+4,i+6,lambda x: 2*x**1 + 3)


for i in range(0,1):
    Trapezoid(i+5,i+7,lambda x: 2*x**1 + 4 )


for i in range(0,1):
    Trapezoid(i+6,i+8,lambda x: 2*x**1 + 5)


for i in range(0,1):
    Trapezoid(i+7,i+9,lambda x: 2*x**1 + 6)


for i in range(0,1):
    Trapezoid(i+8,i+10,lambda x: 2*x**1 + 7)


for i in range(0,1):
    Trapezoid(i+9,i+11,lambda x: 2*x**1 + 8)


for i in range(0,1):
    Trapezoid(i+10,i+12,lambda x: 2*x**1 + 9)


for i in range(0,1):
    Trapezoid(i+11,i+13,lambda x: 2*x**1 + 10)

