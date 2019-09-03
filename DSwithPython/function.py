def absolute(num):
    if num>=0:
        return num
    else:
        return -num

print(absolute(-1))
print(absolute(2))
print(absolute(-5))
print(absolute(5))

def greet(*names):
    for name in names:
        print("Hello "+ name)

greet("shahraaz","Hussain","Mohammed")