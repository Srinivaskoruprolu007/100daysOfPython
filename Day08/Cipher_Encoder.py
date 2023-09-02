import Caesar_Cipher_logo
print(Caesar_Cipher_logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(plain_string, shift_amount):
#     cipher_text = ''
#     for letter in plain_string:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')
#
#
# def decrypt(cipher_text, shift_amount):
#     decrypted_code = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decrypted_code += new_letter
#     print(f"The decrypted code is {decrypted_code}")


def caesar(start_text, shift_amount, choice):
    end_text = ''
    if choice == 'decode':
        shift_amount *= -1
    elif choice == 'encode':
        shift_amount *= 1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        end_text += new_letter
    print()


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift_amount number:\n"))
caesar(text, shift, direction)



