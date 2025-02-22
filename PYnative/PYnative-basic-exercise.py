#Exercise 1
''''''

number1 = 40
number2 = 30

if number1 * number2 <= 1000:
    print(number1 * number2)
else:
    print(f'The result is {number1+number2}')



#Exercise 2 
n = 0
print('Printing current and previous number sum in a range(10)')
for i in range(10):
    print(f'Current Number {i} Previous Number {n} Sum : {i + n}')
    n = i




#Exercise 3




def print_even_index(string):
    n = 0
    for i in string:
        if n % 2 == 0:
           print(i)
        n += 1

print_even_index('assalomu')




#Exercise 4




def remove_chars(word, chars):
   return word[chars:]

print(remove_chars('PYnative',2))




#Exercise 5




numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def first_last_same(numlist):
    if numlist[0] == numlist[-1]:
        return True
    else:
        return False
print('Given list:',numbers_x)
print(f'Result is {first_last_same(numbers_x)}')

print('Given list:',numbers_y)
print(f'Result is {first_last_same(numbers_y)}')




#Exercise 6




l = [10, 20, 33, 46, 55]

def divisible_by5(listnum):
    for i in listnum:
        if i % 5 ==0:
            print(i)

print('Given lis is: ', l)
print('divisible by 5')
divisible_by5(l)




#Exercise 7





s = "Emma is good developer. Emma is a writer"
def find_occurences(str,word):
    return str.count(word)

result = find_occurences(s,'Emma')
print(f'Emma appeared {result} times')




#Exercise 8  ???????????????????????? 



def pattern_maker(num):

    for i in range(num + 1):
        for j in range(i):
            print(i, end = ' ')
        print('\n')

pattern_maker(5)




#Exercise 9




def check_plindrome(n):
    p = n
    check = n < 0
    if check:
        n = abs(n)

    rn = 0
    while n > 0:
        digit = n % 10
        n //= 10
        rn = rn * 10 + digit

    if check:
        rn = -rn  # No need for abs()

    print(f'original number {p}')
    if p == rn:
        print('Yes. given number is palindrome number')
    else:
        print('no. given number is not palindrome number')

check_plindrome(-323)
check_plindrome(323)




#Exercise 10






list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def odd_even_list(l1,l2):
    nl = []
    for i in l1:
        if i % 2 != 0:
            nl.append(i)
    for i in l2:
        if i % 2 == 0:
            nl.append(i)
    return nl

print(odd_even_list(list1,list2))




#Exercise 11

# input: 7536
# output “6 3 5 7“



def digit_reverse_space(num):
    result = ''
    while num > 0:
        digit = num % 10
        num = num // 10
        print(digit, end= ' ')
digit_reverse_space(7536)




#Exercise 12





income = 45000
# 45000
rate = 0
if income >= 10000:
    next = income - 10000 #35000
    rate = 0
    if next <= 10000:    #0
        rate = next * 0.1
    elif next >= 10000: #35000
        remaining = next -10000 #25000
        rate = rate + (10000 * 0.1)
        rate = rate + (remaining * 0.20)
else:
    rate = 0

print(rate)




#Exercise 13





for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = ' ')
    print('\t')




#Exercise 14




for i in range(5,0,-1):
    for j in range(i):
        print('*' ,end=' ')
    print(' ')




#Exercise 15



def exponent(base, exp):
    return base**exp


result = exponent(5,4)
print(result)



