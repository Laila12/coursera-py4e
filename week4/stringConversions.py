a = "123"
print(type(a))

# print(a + 1)  actually gives a TypeError cuz we're essentially adding a string and integer

print(int(a) + 1)


# Throws ValueError: invalid literal for int() with base 10: 'Hello Bob'
# b = "Hello Bob"
# print(int(b) + 1)
