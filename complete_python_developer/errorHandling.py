# program to work with the exception handling of the python code.

while True:
    try:
        age = int(input('What is your age:'))
        print(age)
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print(f'You cannot enter age as {age}')
    else:
        print('Thank you')
        break
    finally:
        print('I am done!')
