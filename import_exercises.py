

#1b
from function_exercises import calculate_tip
print(calculate_tip(50, 10))

import function_exercises

import functions_excercise as fe 
print(fe.get_letter_grade(80))

#2
import itertools

len(list(itertools.product('ABC', '123')))

len(list(itertools.combinations('ABCD', 2)))

len(list(itertools.permutations('ABCD', 2)))


#3
import json 

profiles = json.load(open('profiles.json'))

print(profiles)

# total number of users
print(f"The total number of users is {len(profiles)}")

# number of active users
active_accounts = [accnt for accnt in profiles if accnt['isActive']]
print(f"The total number of active accounts is {len(active_accounts)}")

# number of inactive users
inactive_accounts = len(profiles)- len(active_accounts)
print(f"The total amount of inactive account is {inactive_accounts}")

print(profiles[0])

# total balance of all users
bal_list = []
for accnt in profiles:
    bal_list.append(float(accnt['balance'][1:].replace(',','')))
total_balances = sum(bal_list)
print(f'Total balance in users: ${total_balances}')

# average balance of user
avg_balance=total_balances/len(profiles)
print(f"The average user balance is {avg_balance:.6}")

# user with the lowest balance
min_bal_usr = [accnt for accnt in profiles if float(accnt['balance'][1:].replace(',','')) == min(bal_list)][0] ## [1:] drops the $ and i replace the comma to make a float
print('User with minimum balance is ', min_bal_usr['name'])

# user with the highest balance
max_user = [accnt for accnt in profiles if float(accnt['balance'][1:].replace(',','')) == max(bal_list)][0]
print(f'User with maximum account balance is', max_user['name']) 