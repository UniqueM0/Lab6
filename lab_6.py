"""
To start, we will generate a random integer between 1 and 20, and 
based on the result of the random number, we check to see
if it falls under a certain range
if the number is greater than > 15, then the result will be "Cherries"
otherwise if the number is > 10, then the result will be "orange"
otherwise if the number is > 5, then result will be "plum"
otherwise if the number is > 2, then the result will be "melon"
otherwise if the number is > 1, then the result will be "bell"
if the number is not any of the above, then the result will be "bar"

we iterate over using a loop three times and print the results to the user.
as an example "plum cherries"

"""

"""
import random
num = generate random number 

if num is greater than 15,
    then the result will be "cherries"
otherwise if num is greater than 10,
    then the result will be "orange"
otherwise if num is greater than 5,
    then the result will be "plum"
otherwise if num is greater than 2,
    then the result will be "melon"
otherwise if num is greater than 1,
    then the result will be "bell",
otherwise
    the result will be "bar"

loop three times
    print the output (fruit) to the user
"""


import random


total_earned = 0

def main(total_earned):
    results = []
    for i in range(0, 3):
        results.append(spin())

    print("results", results)#[cherries, orange, bell]
    winner = jackpot(results)

    if(winner):
        print("Winner! You win")
    else:
        print("Sorry try again!")
    
    grand_total = count(results, total_earned) 
    print("grand_total", grand_total)
    option = input("Play again? ")
    if option.lower() == "y" or option.lower == "yes":
        main(total_earned)

def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if(rand_num > 15):
        output = "cherries"
    elif(rand_num > 10):
        output = "orange"
    elif(rand_num > 5):
        output = "plum"
    elif(rand_num > 2):
        output = "melon"
    elif(rand_num > 1):
        output = "bell"
    else:
        output = "bar"


    print(output, end=" ")
    return output 

# spin() can use this method envoke 3 times spin
# spin() do not use function main for this method 
# spin()

def jackpot(results):
    return results[0] == results[1] == results[2]

def count(results, total_earned):
    total = 0
    money_dict = {
        "cherries": (1 * 1000), #multiplying all cherries by 1000
        "orange":(.7 * 100),
        "plum": .6,
        "bell": .4,
        "melon": .2,
        "bar": .1
    }
    for i in results: 
        total += money_dict[i]
    return total_earned + total

main(total_earned)
