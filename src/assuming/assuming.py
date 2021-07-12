class AssumptionException(Exception):
    pass

def assume(assumption, ret=None, msg="Assumption evaluated to False with no specified return value!"):
    def decorator_assume(func):
        from functools import wraps
        @wraps(func)
        def wrapper_assume(*args, **kwargs):
            if assumption(*args, **kwargs):
                return func(*args, **kwargs)
            elif ret is not None:
                return ret
            raise AssumptionException(msg)
        return wrapper_assume
    return decorator_assume

if __name__ == '__main__':
    @assume(lambda x: x > 10)
    def func1(x):
        print(f'{x = }')
    @assume(lambda x: x > 10, -1)
    def func2(x):
        print(f'{x = }')
    @assume(lambda x: x > 10, -1 , "x needs to be greater than 10!")
    def func3(x):
        print(f'{x = }')
    print(f'{func3(10)}')
