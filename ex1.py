#1.1/1.2

print(3 + 1) #4
print(3 * 3) # 9
print(2 ** 3) #8
print("Hello World!") #'Hello World!'

#1.3
print('py' + 'thon') #'python' as the strings concatenate to make a single string
print('py' * 3 + 'thon') #'pypypython' as the 'py' is concatenated 3 times before the addition of 'thon'
#print('py'-'py') #Error as you cannot subtract strings
#print('3' + 3) #Error as one cannot concatenate a sring and an integer
3 * '3' #'333' as it is seen as the string '3' multiplied by 3
#a # error as the variable a has not been declared
a = 3 # no response but now a = 3
a # now 3 is returned as the previous statement made a = 3


#1.4
1 == 1 #True as 1 does equal 1
1 == True #True as 1 represents the boolean True
0 == True #False as 0 represents the boolean value False
0 == False#True, see previous statement
3 == 1 * 3 #True as 1 * 3 == 3
(3 == 1)* 3 #0 as it is boolean value False (represented by 0) multiplied by 3
(3 == 3) * 4 + 3 == 1 #False as 3 == 3 is 1. 1 * 4 + 3 is 7 which is not equal to 1
3 ** 5 >= 4**4 #False as 3 ** 5(243) is not greater than 4 ** 4 (256)


#1.5

5/3 #1.666666667 as division immediately changes ints into floats
5 % 3 #2 as it is the equation of 5 mod 3
5.0 / 3 #1.6666666667
5 / 3.0 #1.66666666667
5.2 % 3 #2.2 as is 5.2 mod 3
2001 ** 200 #a very large number repredenting 2001 to the power of 200


#1.6
#print(2000.3 ** 200) #error as result is too large (float cannot store a number that big)
1.0 + 1.0 - 1.0 #1.0 as the equation was done in floats even though 1.0 is equivilant to 1
1.0 + 1.0e20 - 1.0e20 #0.0 as the number gets so large it hits the limit and then gets subtracted all away

#1.7
name = "John Doe"
print("Hello %s" %(name))

#1.8
float(123) 123.0
float('123') #123.0
float('123.23') #123.23
int(123.23) #123
int('123.23') #error as using string close to float to convert to int
int(float('123.23')) #123 as it is possible to convert float to int with rounding
str(12) #'12'
str(12.2) #'12.2'
bool('a') #true as a is numerically greater than 0
bool(0) #False
bool(0.1) #True


