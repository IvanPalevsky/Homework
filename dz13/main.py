from time import sleep
def cache(func):
    count = 0
    cache_res = None
    def wrapper(*args, **kwargs):
        nonlocal count, cache_res
        count += 1
        if count > 3:
            cache_res = func(*args, **kwargs)
            count = 1
        return cache_res
    return wrapper

@cache
def count(x):
    sleep(2)
    return x ** 3

print(count(2))


