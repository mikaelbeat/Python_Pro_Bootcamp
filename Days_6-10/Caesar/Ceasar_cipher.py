
import Caesar_art as art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_list_size = len(alphabet)

def Caesar(text, shift, direction):
    
    processed_text = ""

    for letter in text:
        if letter not in alphabet:
            processed_text += letter
        else:
            letter_index = alphabet.index(letter)
            
            if shift > alphabet_list_size:
                print(f"Error, maximum value for shift is {alphabet_list_size}.")
                exit()
            elif direction == "encode":
                shift_index = letter_index + shift
            elif direction == "decode":
                shift_index = letter_index - shift
            else:
                print("Please select encode or decode.")
                exit()
            if shift_index < alphabet_list_size:
                processed_letter = alphabet[shift_index]
                processed_text += processed_letter
            else:
                over_index_value = shift_index - alphabet_list_size
                processed_letter = alphabet[over_index_value]
                processed_text += processed_letter
                
    print(f"Processed text is {processed_text}.\n")

def Input_data():
    direction = input("\nDo you want to encode or decode? ")
    while direction != "decode" and direction != "encode":
        direction = input("\nPlease select encode or decode? ")
    text = input(f"Enter text to {direction}: ")
    shift = int(input("Enter shift number: "))
    while shift > alphabet_list_size:
        print(f"Max shift size is {alphabet_list_size + 1}.")
        shift = int(input("Enter shift number: "))
    Caesar(text, shift, direction)


print(art.logo)
Input_data()
again = input("Do you want to convert again? ")
if again == "yes":
    Input_data()
    again = input("Do you want to convert again? ")
else:
    print("Thank you for trying Caesar cipher!")
    


        
        
    
