

direction = input("Syötä: ")
print(f"Direction is {direction}")

while direction != "a" and direction != "b":
    print("Wrong input!")
    direction = input("Syötä uusiks: ")
    print(f"{direction == direction}")
    
print("Loppu")


       
       
