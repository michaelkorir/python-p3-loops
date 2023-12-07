#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter =11
    while counter >0:
        counter -=1
        print(counter)
    print('Happy New Year!')
happy_new_year()

def square_integers(int_list):
    # code goes here!
    return list(map(lambda num: num**2, int_list))
result = square_integers([1,2,3,4,5])
print(result)

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else :
            print(num)
fizzbuzz()