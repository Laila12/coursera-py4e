val = input('Enter a positive number:\n')        # Input is always in the form of <class 'str'>
try:
    val = int(val)
except:
    val = -1

if val >= 0:
    print('Good job! Valid number.')
else:
    print('Invalid input. Not a number.')
