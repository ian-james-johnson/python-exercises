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
g=400
a=380
f=350
print("$",(f*10)+(g*6)+(a*4))

# a student can only be enrolled if the class isn't full
class_is_not_full = True
no_conflict = True
if class_is_not_full and no_conflict:
    print("Enroll in class")

# an offer can only be applied for more than two products and the offer has not expired
more_than_two = True
not_expired = True 
premium_memeber = True
apply_offer=1
no_offer=0
if more_than_two and  not_expired or premium_memeber:
    apply_offer
    print("apply offer")
else:
    no_offer
    print("no offer")