#Output functions
print("Hello world!")

#Input functions
# input('Say Hello : ')



# Variables
my_name = 'Viorel'
print(my_name)
my_number = 1000000
print(my_number)

#Type function
result =type(10)
print(result)

#return of print
result=print('example')
print('example')


#return of input
result=input('Say hello')
print(result)

#print multiple arguments
print('Viorel','Ion' ,'Ilie')

#casting
#result = 'abcd'
#result = int(result)
#print(result)

result=10
result = str(result)
print(type(result))

# Operatii

#comparison

a="abcd"
b="abcd"
print (a==b)
print('Id of a is ' ,id(a))
print('Id of b is ',      id(b))
print (a is b)

#slice
    #0123456789
a = 'my text'
print(a[1])
print(a[1:3])
print(a[1:6])
print(a[1:])
print(a[:6])

print(a[:6:2])

    #-7-6-5-4-3-2-1
#a = ' m y  t e x t'
 #0123456789
a = 'my text'
print(a[-1])
print(a[-1:-6:-1])

b='This is my reversed text'
print(b[::-1])

#String and String methods
my_var = 'Emanuel'

my_str = u"abcd {}"
print(my_str)
my_str = f"My name is {my_var}"
print(my_str)

my_str= r"abcd {} \n \{"
print(my_str)
