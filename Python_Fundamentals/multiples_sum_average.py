#### Multiples ####
# Part I
# Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list.
for n in range(1,1000):
    if (n%2!=0):
        print n

# Part II
# Create another program that prints all the mulitples of 5 from 5 to 1,000,000
for m in range(5,1000000):
    if (m%5==0):
        print m



#### Sum list ####
# Create a program that prints the sum of all values in the list: a = [1,2,5,10,255,3]
a = [1,2,5,10,255,3]
sum = 0

for o in a:
    sum += o

print sum

#### Average list ####
# Create a program that prints the average of the values in the list: a = [1,2,5,10,255,3]
avg = sum/len(a)

print  avg
