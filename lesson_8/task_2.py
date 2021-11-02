class MyZeroDivisionError(Exception):
    pass


while True:
    ab = input('Enter two numbers by space or q to exit: ')
    if ab == 'q':
        break
    try:
        a, b = map(int, ab.split())
        if b == 0:
            raise MyZeroDivisionError()
        print(a / b)
    except MyZeroDivisionError:
        print('The divisor cannot be zero')
    except:
        print('Invalid input')
