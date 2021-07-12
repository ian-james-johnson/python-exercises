#create list of movies and rental times, then calculate cost for the rentals
rental = dict( name = ['The Little Mermaid', 'Brother Bear', 'Hercules'], days = [3, 5, 1])
print('Days that the moveies are rented:')
print(rental['days'])
print('Sum of days rented:')
sum_days = sum( rental['days'])
print(sum_days)
print('Price for the rentals:')
price = sum_days * 3
print(price)

#create a list of pay rates and hours worked, then calculate the money earned
pay_info = { 'employer' : ['Google', 'Amazon', 'Facebook'], 'pay_rate' : [400, 380, 350],
            'hours_worked' : [6, 4, 10] }
x = pay_info['pay_rate']
x = x * 10
print x
print type(x[0:0])

x_int = x
x_int = ( int(i) for i in x_int )
x_int = x_int *10
print x_int

#HAVING PROBLEMS BECAUSE MY NUMBERS FOR PAY AND HOURS ARE TYPE STRING
p = [ int(i) for i in pay_info['pay_rate'] ]
h = [ int(i) for i in pay_info['hours_worked'] ]
earnings = p * h
print earnings

print 'These are the employers:', pay_info['employer']
print 'These are the pay rates:', pay_info['pay_rate']
print 'These are the hours worked:', pay_info['hours_worked']
earnings = pay_info['pay_rate'] * pay_info['hours_worked']
print(earnings)

p = pay_info['pay_rate']
h = 'hours_worked'
print type(pay_info['pay_rate'])
p = int(i) for i in pay_info['pay_rate']
print type(pay_info['pay_rate'])



earnings = p * h
print earnings

print(pay_info)
print(pay_info:hours_worked)
earnings = (pay_rate * hours_worked for employer in pay_info)
print(earnings)
pay_info = {employer : 'google', pay_rate : 400, hours_worked : 6}
print(pay_info)
