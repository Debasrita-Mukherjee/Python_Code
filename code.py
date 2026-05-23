'''def greet():
    print("Hello")

greet()

def square(x):
    return x*x
x= square(17)
print(x)

def greet(name):
    print("Hello: ", name)
greet("Debasrita")
greet("Jit")
greet("Tarunima")'''

def count_even(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            print(i)
            count+=1
    return count
result= count_even(10)
print(result)