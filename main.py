# main.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

if __name__ == "__main__":
    print("Dodawanie: 2 + 3 =", add(2, 3))
