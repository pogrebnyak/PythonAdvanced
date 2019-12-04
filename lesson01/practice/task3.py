for number in range(1,101):
    if not number % 15:
        print('FizzBuzz')
    elif not number % 5:
        print('Buzz')
    elif not number % 3:
        print('Fizz')
    else:
        print(number)