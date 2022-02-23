
print("*** Treasure Island Adventure ***\n")

print("You landed to shore, it is possible to go left or right.")
course = input("Which direction you would like to go? ").lower()

if course == "left":
    print("Game over!")
    exit()
else:
    print("\nYou arrive at house which has three doors?")
    course = input("Which door you choose 1, 2 or 3? ")

if course == "1":
    print("\nGreat job you found the treasure!")
else:
    print("\nBad luck, no trease there. Try again.")
    print("Game over!")

