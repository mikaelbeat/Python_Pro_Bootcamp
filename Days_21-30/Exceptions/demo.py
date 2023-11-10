
FILE_LOCATION = "Days_21-30/Exceptions/"

try:
    file = open("demo.txt")
except:
    print("File not found.")
    print("Creating file.")
    with open(f"{FILE_LOCATION}demo.txt", "w") as data_file:
        data_file.write("Huhhelihei")
finally:
    print("Writed to file.")