#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please tell me your name:")

    ## the line below creates a single string that is passed to print()
    # print("You told me your name is: " + user_input)

    ## collect the day of the week from the user
    day_input = input("What day of the week is it:")

    # greet the user and tell them the day of the week)
    print("Hello", user_input, "Happy", day_input,"!")

main()
