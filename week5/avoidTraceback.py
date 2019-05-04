val = 'Hello Bob'
try:
    convertVal = int(string)
except:
    convertVal = -1
print('First val:', convertVal)

val = "123"
try:
    convertVal = int(val)
except:
    convertVal = -1
print('Second val:', convertVal)
