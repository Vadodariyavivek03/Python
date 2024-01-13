# String Format

x = '{} , my name is vivek and i am from {}, Gujrat, {}'
y = x.format('Hello!','Rajkot','India.')
print(y)
print(x.format('Hi','ABC','XYZ'))

print('-------------------------------------------------------------------------------')
# We can specify index in format like,

x = '{1} , my name is vivek and i am from {2}, Gujrat, {0}'
y = x.format('Hello!','Rajkot','India.')
print(y)
print(x.format('Hi','ABC','XYZ'))

print('-------------------------------------------------------------------------------')
#We can specify alias base on key:value pair like,

x = '{Greeting} , my name is vivek and i am from {city}, Gujrat, {country}'
y = x.format(Greeting='Hello!', city='Rajkot',country='India.')
print(y)

