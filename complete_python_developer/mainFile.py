def sumFive(num1):
    try:
        if num1:
            return num1 + 5
        else:
            return 'Please enter the number'
    except TypeError as err:
        return err
