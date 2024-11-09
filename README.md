# Simple Encryption and Decryption Program

## How the Algorithm Works

This program implements a simple substitution cipher for encrypting and decrypting text.

1. **Character Set**: The program uses a character set that includes spaces, punctuation, digits, and ASCII letters.
2. **Key Generation**:

   - For each encryption, a new key is generated.
   - The key is a randomly shuffled version of the character set.
3. **Encryption**:

   - For each character in the plain_text:
     - Find its index in the original character set.
     - Replace it with the character at the same index in the key.
4. **Decryption**:

   - For each character in the cipher_text:
     - Find its index in the key.
     - Replace it with the character at the same index in the original character set.
5. **File Storage**:

   - The encrypted text and the key are stored together in a JSON structure.
   - This JSON is then encoded in base64 to ensure safe storage in text files.

## Steps to Run the Program

### Verifying Python Installation

Before running the program, you should verify that Python is installed on your system. Here's how you can do this:

1. Open a terminal or command prompt on your computer.
2. Type the following command and press Enter:

   ```
   python --version
   ```
3. If Python is installed, you'll see output similar to this:

   ```
   Python 3.12.3
   ```

   (The exact version number may differ)
4. If you see an error message or the version is lower than 3.6, you'll need to install or update Python.

   * To install Python, visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   * Download and run the installer appropriate for your operating system.
5. After installation, close and reopen your terminal, then repeat steps 2-3 to verify the installation.

### Running the Program

Once you've verified that Python (version 3.6 or later) is installed:

1. Save the `cipher.py` file to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `cipher.py`. You can use the `cd` command to change directories. For example:

   ```
   path/to/directory
   ```
4. Run the program by typing:

   ```
   python cipher.py
   ```
5. Follow the on-screen prompts to encrypt or decrypt messages.

   ```
   1. Create an encrypted file
   2. Encrypt an existing text file
   3. Decrypt a file
   4. Exit
   Enter your choice (1-4): 
   ```

## User Guide

### Encrypting a Message

#### Option 1: Create an encrypted file from input

1. Run the program and choose option 1: "Create an encrypted file from input"
2. Enter a name for your encrypted file (don't include .txt, it will be added automatically).
3. Type or paste the message you want to encrypt.
4. The program will display your original message and the encrypted version.
5. The encrypted file will be saved in the same directory as the program.

#### Option 2: Encrypt an existing text file

1. Run the program and choose option 2: "Encrypt an existing text file"
2. Enter the full name of the file you want to encrypt (including .txt).
3. Enter a name for the encrypted output file (don't include .txt, it will be added automatically).
4. The program will display the name of the original file and the name of the encrypted file.
5. The encrypted file will be saved in the same directory as the program.

### Decrypting a Message

1. Run the program and choose option 2: "Decrypt a file"
2. Enter the full name of the file you want to decrypt (including .txt).
3. The program will display the encrypted message and its decrypted version.
4. You'll be asked if you want to save the decrypted text to a file
   * If yes, enter a name for the decrypted file (don't include .txt).

### Tips for Users

* Always keep your encrypted files secure. Anyone with access to the file can decrypt it using this program.
* If you're sending an encrypted message to someone, they'll need this program to decrypt it.
* The program can handle spaces and punctuation, so feel free to write naturally.
* If you get an error while decrypting, make sure you're using a file that was encrypted with this specific program.

## Troubleshooting

If you encounter issues running the program:

1. Ensure you're in the correct directory containing `cipher.py`.
2. Try using `python3` instead of `python` if you're on macOS or Linux:

   ```
   python3 cipher.py
   ```
3. If you get a "Module not found" error, double-check that you're using a Python version 3.6 or later, as the program uses f-strings which are not available in earlier versions.
