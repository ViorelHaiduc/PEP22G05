#String and String methods
my_var = 'Emanuel'

my_str = u"abcd {}"
print(my_str)
my_str = f"My name is {my_var}"
print(my_str)

my_str= r"aBcD {0} \n \{0}"
print(my_str)


result = my_str.split()
print(type(result))
print(result)

result = my_str.format('x' ,'y')
print(result)

result = my_str.center(80)
print(result)


result = my_str.lower()
print(result)

result = my_str.upper()
print(result)