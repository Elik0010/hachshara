#12.1
def power_of(base, power):
    if power == 1:
        return base
    return base * power_of(base, power - 1)

print(power_of(3,4))

#12.2
def addition(n):
   return n + n


def even(n):
    if n % 2:
        return False
    return True

def myrecmap(func, items):
    if len(items) == 1:
        return [func(items[0])]
    else:
        return [func(items[0])] + myrecmap(func, items[1:])


n = [1,2,3,4,5,6,7,8,9,10]
print(myrecmap(addition,n))


def myrecfilter(func, items):
    if len(items) == 1:
        if func(items[0]):
            return [items[0]]
        else:
            return []
    else:
        if func(items[0]):
            return [items[0]] + myrecfilter(func, items[1:])
        else:
            return myrecfilter(func, items[1:])
print(myrecfilter(even, n))


#12.3
def purify_iter(items):
    result = []
    for i in items:
        if not i % 2:
            result.append(i)
    return result


def purify_rec(items):
    result = items[:]
    if len(result) == 1:
        if not result[0] % 2:
            return [result[0]]
        else:
            return []
    else:
        if not result[0] % 2:
            return [result[0]] + purify_rec(result[1:])
        else: 
            return purify_rec(result[1:])
            

#12.4
def prod_iter(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

def prod_rec(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] * prod_rec(numbers[1:])


#12.5
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(12))

#12.6
import sys
import numpy as np
def root_rec(f, a, b, stp = 1):
    if a > b:
        a,b = b,a
    for i in np.arange(a,b + stp, stp):
        if f(i) < 0 and f(i + stp) > 0:
            return root_rec(f, i, i + stp, stp / 10)
        elif f(i) > 0 and f(i - stp) < 0:
            return root_rec(f, i, i - stp, stp / 10)
        elif f(i) == 0:
            return i
    
    if abs(f(a)) > abs(f(b)):
        return root_rec(f, b, b + (b - a), stp)
    else:
        if stp < 0.000000000001:
            return (a+b)/2
        return root_rec(f, a - (b - a), a, stp)


def func(a):
    return a ** 2 + 5 * a - 3
print(root_rec(func, 10, 30))


#12.9
def palindrome(word):
    for i in range(len(word)):
        if len(word) == 0:
            return ""
        if word[i] != word[-(i + 1)]:
            if len(word) == 2:
                return word[0]

            return max(palindrome(word[:i] + word[i + 1:]), palindrome(word[:-(i + 1)] + word[-i:] if i > 0 else []), key = len)
        
    return word


def palindrome2(word, palin = ""):
    result = palin
    while True:
        if len(word) == 0:
            return result + result[::-1]
        if len(word) == 1:
            return result + word + result[::-1]
        if word[0] != word[-1]:
            if len(word) == 2:
                return result + word[0] + result[::-1]

            return max(palindrome2(word[1:], result), palindrome2(word[:-1], result), key = len)
        else:
            result += word[0]
            word = word[1:-1]
    return result + result[::-1]

# print(palindrome2('dhwjigolkaajduekdokhdshd'))
# print(palindrome('dhwjigolkatskdjewakdokhdshd'))



#12.10
import random
def quick_rec(numbers):
    if len(numbers) == 1 or len(numbers) == 0:
        return numbers
    list_u = []
    list_o = []
    list_b = []
    pivot = random.choice(numbers)
    for i in numbers:
        if i > pivot:
            list_o.append(i)
        elif i < pivot:
            list_u.append(i)
        else:
            list_b.append(i)
    if list_o == [] and list_u == []:
        return list_b
    return quick_rec(list_u + list_b) + quick_rec(list_o)

print(quick_rec([4,8,7,6,5,9,8,5,4,2,3,4,6,8,9,5,4,7]))

