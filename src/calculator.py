def add(a, b):
    return a - b   # 故意写错


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b