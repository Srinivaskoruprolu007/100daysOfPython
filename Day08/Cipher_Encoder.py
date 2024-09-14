import Caesar_Cipher_logo
print(Caesar_Cipher_logo.logo)  # Print the logo from the Caesar_Cipher_logo module

# Define the alphabet with a wrap-around for shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, choice):
    """
    Encrypt or decrypt a text using the Caesar cipher.
    
    :param start_text: The text to be encoded or decoded.
    :param shift_amount: The number of positions each letter in the text is shifted.
    :param choice: 'encode' to encrypt, 'decode' to decrypt.
    """
    end_text = ''  # Initialize the resulting text
    
    # Adjust shift amount for decoding
    if choice == 'decode':
        shift_amount *= -1
    
    # Process each letter in the text
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)  # Find the position of the letter in the alphabet
            # Calculate the new position with wrap-around
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]  # Get the letter at the new position
            end_text += new_letter  # Add the new letter to the resulting text
        else:
            end_text += letter  # Non-alphabet characters remain unchanged
    
    # Print the resulting encoded or decoded text
    print(f"The {choice}d text is {end_text}")

# User input for Caesar cipher operation
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift_amount number:\n"))

# Call the Caesar cipher function with user inputs
caesar(text, shift, direction)