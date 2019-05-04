# If either one of the conditions is true then the program sequence doesn't execute other consecutive elif or else

x = 5
if x < 2:
    print('Small')
elif x < 10:        # elif essentially means else if
    print('Medium')
else:
    print('Large')
print('All Done')
