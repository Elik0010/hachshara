#Control Flow
#2.1
range(5) #range(0,5) object. for i in range(5) means for each number from 0 to 4 inclusive
type(range(5)) #<class 'range'>


#2.2
for i in range(101):
	print(i)

for i in range(0, 101, 7):
	print(i)
	
for i in range(0, 101, 5):
	if i % 3:
		print(i)
		
for i in range(2,21):
	print("Number: %s" % (i))
	for j in range(2, i):
		if not i % j:
			print(j)
			
			
#2.3 
i = 0
while(i <= 100):
	print(i)
	i += 1
	
i = 0
while(i <= 100):
	if not i % 7:
		print(i)
	i += 1
	
#2.4 NOT RELEVANT

#2.5
i = 11
num_found = 0
while num_found<20:
	if i % 7 and i % 5:
		print(i)
		num_found += 1
	i += 11
	
	
i = 10
num_not_found = True

while num_not_found:
	for j in range(1,10):
		num_not_found = False
		if i % j:
			num_not_found = True
			break
	i += 10
	
i = i - 10
print(i) #2520


#2.7
i = 1030
while not i == 1:
	print(i)
	if not i % 2:
		i = i/2
	else:
		i = 3 * i + 1


