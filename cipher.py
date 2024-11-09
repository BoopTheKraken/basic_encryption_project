# --------------------------------------------------------------------------------------
# Name: Tatiana Klimova
# Class: CPSC253
# Assignment: Project 1
# Scope: Program that encrypts and decrypts text files using a self-designed algorithm.
# --------------------------------------------------------------------------------------

import random
import string
import json
import base64

# Creates character set for the encryption/decription use
chars = " " + string.punctuation + string.digits + string.ascii_letters + "\n"
chars = list(chars)

# Generate a random encryption key
#   - use shuffled copy of the characters as encryption key.
def generate_key():
    key = chars.copy()
    random.shuffle(key)
    return ''.join(key)

# Encrypt input text using they key
# - for each character in the text, finds its index in the original char set.
# - replace it with the character at the same index in they key
def encrypt(text, key):
    cipher_text = ""
    for letter in text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

# Decrypt text using provided key
# - for each char in encrypted text, find its index in the key.
# - replace it with the char at the same index in the original char set.
def decrypt(text, key):
    plain_text = ""
    for letter in text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text


# Create a mew file with encrypted content.
#  - generate new encryption key
#  - encrypt input text
#  - save both encrypted text and the key in JSON structure (probably not the best practice, but the best one I could think of that worked)
#  - encode JSON as base64 and write to file.txt
def create_encrypted_txt_file():
    filename = input("\nEnter the name for encrypted text file (without .txt): \n")
    filename = filename.strip() + ".txt"

    try:
        plain_text = input("\nEnter the message to encrypt: \n")
        key = generate_key()
        cipher_text = encrypt(plain_text, key)
        
        # Create a dictionary with the encrypted text and the key
        data = {
            "cipher_text": cipher_text,
            "key": key
        }
        
        # Convert the dictionary to a JSON string, encode it in base64, and decode back to string        
        encoded_data = base64.b64encode(json.dumps(data).encode()).decode()
        
        with open(filename, 'w') as file:
            file.write(encoded_data)
        
        print(f"\nFile '{filename}' has been created successfully with the encrypted message.\n")
        print(f"\nOriginal message: {plain_text}\n")
        print(f"\nEncrypted message: {cipher_text}\n")
    # Error exceptions handlers
    except IOError:
        print(f"\nAn error occurred while creating the file '{filename}'.")
    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")

# Decreypt the text inside .txt file and save decrypted text if desired.
#   - reads and decodes the base64 encoded data from the file, parsing the JSON to extract the text and the key
#   - uses the extracted key to decrypt the cipher text
def decrypt_file():
    input_filename = input("\nEnter the name of the file to decrypt (including .txt): ")
    try:
        with open(input_filename, 'r') as file:
            encoded_data = file.read()
        
        # Decodes the base63 data/text and parses the JSON
        data = json.loads(base64.b64decode(encoded_data).decode())
        cipher_text = data['cipher_text']
        key = data['key']
        
        plain_text = decrypt(cipher_text, key)
        print(f"\nEncrypted message: {cipher_text}")
        print(f"\nDecrypted message: {plain_text}\n")
        
        # Ask user if they want to save the decrypted text
        save_choice = input("Do you want to save the decrypted text to a file? (y/n): ").lower()
        if save_choice == 'y':
            output_filename = input("Enter the name for the decrypted text file (without .txt): ")
            output_filename = output_filename.strip() + ".txt"
            
            # Error/exception handlers
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(plain_text)
                print(f"\nDecrypted text has been saved to '{output_filename}' successfully.")
            except IOError:
                print(f"\nAn error occurred while saving the decrypted text to '{output_filename}'.")
            except Exception as error:
                print(f"\nAn unexpected error occurred while saving: {error}")
        
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
    except json.JSONDecodeError:
        print("The file is not in the correct format.")
    except KeyError:
        print("The file does not contain the required encryption data.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

# Read and encrypt a plain text file
#   - Reads a plain .txt file
#   - saves file.txt with encrypted text.
def encrypt_file():
    input_filename = input("\nEnter the name of the file to encrypt (including .txt): ")
    try:
        with open(input_filename, 'r') as file:
            plain_text = file.read()
        
        key = generate_key()
        cipher_text = encrypt(plain_text, key)
        
        data = {
            "cipher_text": cipher_text,
            "key": key
        }
        
        encoded_data = base64.b64encode(json.dumps(data).encode()).decode()
        
        output_filename = input("Enter the name for the encrypted file (without .txt): ")
        output_filename = output_filename.strip() + ".txt"
        
        with open(output_filename, 'w') as file:
            file.write(encoded_data)
            
        print(f"\nOriginal message:\n {plain_text}\n")
        print(f"\nEncrypted message:\n {cipher_text}\n")        
        print(f"\nFile '{output_filename}' has been created successfully with the encrypted content.")
 
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
    except IOError:
        print(f"\nAn error occurred while reading or writing the file.")
    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")


def main():
    # Menu options for the use
    #   - calls appropriate functions based on 1-4 selection input.
    while True:
        print("\n1. Create an encrypted file from input")
        print("2. Encrypt an existing text file")
        print("3. Decrypt a file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_encrypted_txt_file()
        elif choice =='2':
            encrypt_file()
        elif choice == '3':
            decrypt_file()
        elif choice == '4':
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
    
    
# Resources
# https://www.youtube.com/watch?v=mxwvvMZaIvU
# https://www.youtube.com/watch?v=1WYn1DO9emg
# https://ioflood.com/blog/python-base64-encode/
# https://gist.github.com/khornberg/b87e4a72532a342e1e5ebb16b5739e8f
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/stdtypes.html


