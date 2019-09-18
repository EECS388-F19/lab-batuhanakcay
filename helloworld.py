import random

print("Batuhan")
sum=0
for x in range(2):
	randnum=random.randint(1,100)
	print (str(randnum))
	sum=sum+randnum
print("Sum= %s" %(sum))
print("Average= " + str(sum/2.0)) 

