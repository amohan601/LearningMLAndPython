
def add(a,b):
    return a+b

import operator

def add2(a,b):
    return operator.add(a,b)

add3 = lambda x,y: x+y

if __name__== '__main__':

    try:

        a = int(input('Enter first number : '))
        b = int(input('Enter second number : '))
        print('Sum(simple) of {} + {} =  {} '.format(a, b, add(a,b)) )
        print('Sum(using operator) of {} + {} =  {} '.format(a, b, add2(a,b)) )
        print('Sum(using lambda) of {} + {} =  {} '.format(a, b, add3(a,b)) )

    except ValueError:
        print('invalid value given in the input')