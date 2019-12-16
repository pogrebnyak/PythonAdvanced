import time

def decorator(num_of_repeats):
    def actual_decorator(func):
        def wrapper():
            start = time.time()
            for i in range(num_of_repeats):
                print(func())
            end = time.time()
            sum_time = end - start
            print(sum_time)

            return func.__name__

        return wrapper

    return actual_decorator


@decorator(100)
def my_func():
    return 'Hello World!'

print(my_func())