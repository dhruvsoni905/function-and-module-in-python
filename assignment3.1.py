'''

def factorial(n=int(input("enter a number:"))):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

result = factorial()

print("The factorial  is:",result)
'''

