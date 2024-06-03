from cipher_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def ceasar(text,shift):
    if direction == "decode":
        shift = -shift
    
    modified_text = ""
    for i in range(0,len(text)):
        letter = text[i]
        if(letter == ' '):
            modified_text += " "
            continue
        idx_new_letter = (alphabet.index(letter)+shift)%26
        modified_text += alphabet[idx_new_letter]
    print(f"The encoded text is {modified_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text,shift)
    test= input("Do you want to go again? Type 'yes' or 'no'.")
    if test.lower() == "no":
        break


