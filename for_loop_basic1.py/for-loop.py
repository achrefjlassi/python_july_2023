#print all integer between 1 and 150:
for x in range(1, 151):
  print(x)
# Print all the multiples of 5 from 5 to 1,000
for x in range(1,1001):
  if (x % 5 == 0):
    print(x)
# Print integers 1 to 100.
#  If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101):
  if (x%5==0 )&( x%10!=0):
    print("coding")
  elif (x%10==0):
    print("coding dojo")
  else:
    print(x)
# Add odd integers from 0 to 500,000, and print the final sum.
for x in range(0,500000):
  sum=0
  if(x%2!=0):
    sum=sum+x

# print("The sum of the numbers is:", sum)
# Print positive numbers starting at 2018, counting down by fours.
for x in range(-2018,0):
  if(x%4==0):
    print(-x)

  