# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit3-08.py File,
# learning nested if statements in python.

 
def main():

    # input and variables
    year = input("Enter the year: ")

    # process and output
    print("")
    try:
        year = int(year)
        if year % 4 == 0:
            if year % 400 == 0:
                print("That is a leap year.")
            elif year % 100 == 0:
                print("That is a regular year.")
            else:
                print("That is a leap year.")
        else:
            print("That is regular year.")
    except ValueError:
        print("Invalid input, Please try again following the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
