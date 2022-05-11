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

def main():
    for i in range(0, 3):
        spin()

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

# spin() can use this method envoke 3 times spin
# spin() do not use function main for this method 
# spin()

main()
