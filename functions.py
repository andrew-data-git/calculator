'''Functions to be called by calculator app'''

def add(x: float, y: float) -> float:
    return x + y

def minus(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise Exception('Division by zero is not allowed')
    return x / y

def raise_to(x: float, y: float) -> float:
    return x ** y
