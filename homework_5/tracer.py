def trace(func):
    depth = 0
    def wrapper(*args, **kwargs):
        nonlocal depth
        print("->" * depth,  f'{func.__name__}({args[0]})') # вход с отступом

        depth += 1
        result = func(*args, **kwargs)
        depth -= 1

        print("<-" * depth, f'{func.__name__}()={result}') # выход с отступом
        return result
    return wrapper