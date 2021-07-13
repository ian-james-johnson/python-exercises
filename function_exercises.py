#1 create a function that accept one input and gives True if it is a 2 number or string, and false otherwise
def is_two(n):
    if int(n) == 2:
        result = True
    else:
        result = False
    return result

outcome = is_two(2)

#2 create a function that takes a string and returns True if that string is a vowel
def is_vowel(character):
    if str.lower(character) in ('e', 'u', 'i', 'o', 'a'):
        result = True
    else:
        result = False
    return result

result = is_vowel('e')
print(result)

#3 modify is_vowel to return True for consonants and False otherwise
def is_consonant(character):
    if str.lower(character) in ('q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'):
        result = True
    else:
        result = False
    return result

x = is_consonant('a')
print(x)

#4 create a function that accepts a word as a string, then capitalizes the first letter of the word if it is a consonant
def function_4(word):
    first = word[0]
    if first in ('q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'):
        word = str.upper(word[0]) + word[1:]
    return word

print(function_4('bye'))

#5 create a function that accepts a bill total and a tip percentage, and then returns a tip amount
def calculate_tip(bill, tip_percent):
    tip_amount = bill * (tip_percent / 100)
    return tip_amount

print(calculate_tip(10, 10))

#6 create a function that accepts an original price and a discount percentage, and then returns a discounted price
def apply_discount(original_price, discount_percentage):
    discount_price = original_price - (original_price * (discount_percentage / 100))
    return discount_price

print(apply_discount(100, 10))

#7 create a function that accepts a string containing commas, and then counts the commas as output
def handle_commas(str_input):
    counter = 0
    for character in str_input:
        if character == ',':
            counter += 1
    return counter

print(handle_commas('qwerty,qwerty,qwerty,qwerty,'))

#8 create a function that accepts a number grade and returns a letter grade
def get_leter_grade(score):
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
    return grade

print(get_leter_grade(90))

#9 create a function that accepts a string and returns a string with the vowels removed
def remove_vowels(word):
    new_word ='' 
    for letter in word:
        if str.lower(letter) not in ('euioa'):
            new_word = new_word + letter
    return new_word

print(remove_vowels('hello'))

#10 create a function that will turn a string into a normalized name following common naming conventions
def normalize_name(name):
    name = str.lower(name)
    normalized_name = ''
    for letter in name:
        if letter == ' ':
            letter = '_'
        if letter in ('qwertyuiopasdfghjklzxcvbnm_1234567890'):
            normalized_name = normalized_name + letter
    return normalized_name

print(normalize_name('Ian Johnson!!!'))

#11 create a function that accepts a list of numbers and returns list of cumulative numbers
def cumulative_sum(num_list):



    