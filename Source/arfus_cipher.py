import random
import string
import json
import os

def generate_shuffled_alphabet(key: str) -> str:
    random.seed(key)
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def ArfusCipherEncoder(text: str, key: str) -> str:
    shuffled_alphabet = generate_shuffled_alphabet(key)
    encoded_text = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encoded_char = shuffled_alphabet[ord(char) - ord('a')]
            if is_upper:
                encoded_char = encoded_char.upper()
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def ArfusCipherDecoder(text: str, key: str) -> str:
    shuffled_alphabet = generate_shuffled_alphabet(key)
    decoded_text = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decoded_char = chr(shuffled_alphabet.index(char) + ord('a'))
            if is_upper:
                decoded_char = decoded_char.upper()
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text

def save_to_json(data: dict, filename: str):
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    file_path = os.path.join(desktop, filename)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"File saved to {file_path}")

print("-------------------Welcome TO Arfus Cipher--------------")

while True:
    print("\n1-Encoder \n2-Decoder \n3-Exit\n\nEnter your option:")
    try:
        option = int(input().strip())
    except ValueError:
        print("Enter a valid number for option.")
        continue

    if option not in [1, 2, 3]:
        print("Enter a valid option.")
        continue

    if option == 1:
        original_text = input("Enter your text: ").strip()
        key = input("Enter your key (word): ").strip()
        crypted_text = ArfusCipherEncoder(original_text, key)
        print("Your encoded text: " + crypted_text)
        save_to_json({"original_text": original_text, "encoded_text": crypted_text, "key": key}, "encoded_text.json")

    elif option == 2:
        encrypted_text = input("Enter the encoded text: ").strip()
        key = input("Enter your key (word): ").strip()
        decrypted_text = ArfusCipherDecoder(encrypted_text, key)
        print("Your decoded text: " + decrypted_text)
        save_to_json({"encoded_text": encrypted_text, "decoded_text": decrypted_text, "key": key}, "decoded_text.json")

    elif option == 3:
        break
