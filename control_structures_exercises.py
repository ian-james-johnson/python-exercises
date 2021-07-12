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

#2b prompt user for a number, then show a multiplication table up through 10 for that number
print('Input a number')
number = input()
for i in range(0, 11)
product = number * i
print(f"{number} * {i} = {product}")
i += 1
