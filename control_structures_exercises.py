#1a prompt the user for the day of the week, and print out whether the day is monday or not
print("What day of the week is it?")
day_of_the_week = input()
if day_of_the_week == 'monday':
    print('Today is monday')
else:
    print('Today is not monday')

#1b prompt the user for the day of the week, and print whether it is a weekday or the weekend
print("What day of the week is it?")
day_of_the_week = input()
if day_of_the_week == 'monday' or day_of_the_week == 'tuesday' or day_of_the_week == 'wednesday' or day_of_the_week == 'thursday' or day_of_the_week == 'friday':
    print('Today is a weekday')
elif day_of_the_week == 'saturday' or day_of_the_week == 'sunday':
    print('Today is the weekend')
else:
    print('You did not input a real day')

#1c create variable for a salary, and then calculate weekly paycheck
hours_per_week = 80
hourly_rate = 50
overtime = 1.5
if hours_per_week <= 40:
    weekly_pay = hours_per_week * hourly_rate
    print(weekly_pay)
else:
    weekly_pay = hours_per_week * hourly_rate * overtime
    print(weekly_pay)

#2a create a while loop that iterates an increasing i
i=5
while i <= 15:
    print(i)
    i += 1

#create a while loop starting at 0 and counting even numbers until 100, print each iteration
i = 0
while i <= 100:
    print(i)
    i += 2

#make a while loop that counts backwards by 5's starting from 100 to -10
i = 100
while i >= -10:
    print(i)
    i += -5

#make a while loop that starts at 2 and gets squared at each iteration until reaching 1000000
i = 2
while i < 1000000:
    print(i)
    i = i ** 2

#write a loop that recreates the given pattern in the list
i = 100
while i > 0:
    print(i)
    i = i - 5

#2bi prompt user for a number, then show a multiplication table up through 10 for that number
print('Input a number')
number = input()
for i in range(0, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
    i += 1

#2bii creat a for loop that prints the equivalent of an example table (given in exercise worksheet)
for i in range(1, 10):
    str_i = str(i)
    print(str_i * i)
    i += 1

#2ci prompt user for an odd number between 1 and 50. use a loop and break to to continue prompting the user if input is invalid
i = 1
while i <= 10:
    n = input()
    n = float(n)
    if (n % 2 != 0) and ((n >= 1) and (n <= 50)):
        break

# use loop and continue to count odd numbers between 1 and 50 while skipping "n"
print("The number to skip is : ", n)
for i in range(1,50):
    if (i != n) and (i % 2 != 0):
        print(i)
        continue

#2d prompt use for n, and use a loop to count from 0 to n
n = input()
n = int(n)
if type(n) == int:
    for i in range(0, n + 1):
        print(i)
        i += 1

#2e prompt for a positive integer n, then write a loop that prints the integers between n and 1 (inclusive)
n = input()
n = int(n)
if type(n) == int:
    for i in range(1, n + 1):
        print(i)
        i += 1

#3 fizzbuzz test, fizz for divisible by 3, buzz for divisible by 5, otherwise print i from 1 to 100
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)

#4 prompt for n, for int between i and n; show i, i^2, and i^3
n = input()
n = int(n)
for i in range(1, n + 1):
    sq = i ** 2
    cb = i ** 3
    print(i, sq, cb)

#5 convert number grades into letter grades for prompted test score
while True:
    print("Input 'yes' if you wish to continue or 'no' if you are finished")
    prompt_yn = input()
    if str.lower(prompt_yn) == 'no':
        break
    elif str.lower(prompt_yn) != 'yes':
        continue
    else:
        print("Enter score")
        score = int(input())
        if score <= 100 and score >= 88:
            grade = 'A'
        elif score <= 87 and score >= 80:
            grade = 'B'
        elif score <= 79 and score >= 67:
            grade = 'C'
        elif score <= 66 and score >= 60:
            grade = 'D'
        elif score <= 59 and score >= 0:
            grade = 'F'
        else:
            grade = 'Score is out of expected range'
    print(grade)
    continue
