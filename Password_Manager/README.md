# 🔐 Password Manager

A simple command-line password manager written in Python.

This project allows users to securely store and retrieve passwords using symmetric encryption with the `cryptography` library.

## Features

- ➕ Add new username and password entries
- 🔒 Encrypt passwords before saving them
- 🔑 Decrypt passwords when viewing stored credentials
- 💾 Store encrypted passwords in a text file
- 🖥️ Simple command-line interface

## Technologies Used

- Python
- cryptography (Fernet)

## Project Structure

```
.
├── password_manager.py
├── password_3.txt      # Stores encrypted passwords
└── mykey_3.key         # Encryption key
```

## How It Works

1. A secret encryption key is generated once and saved to a key file.
2. When a new password is added:
   - The password is encrypted using Fernet.
   - The encrypted password is stored in a text file.
3. When viewing passwords:
   - The encrypted passwords are read from the file.
   - They are decrypted using the same key before being displayed.

## Example

```
Choose a Mode; v:view, a:add, q:quit

a
Enter a new username: alice
Enter a new password: MyPassword123

Password added successfully!
```

## Notes

This was one of my early Python projects created for learning purposes.

The project focuses on:
- File handling
- Functions
- Basic encryption and decryption
- Working with external Python packages

It is **not intended for production use**, as the encryption key is stored locally alongside the encrypted passwords and additional security features are not implemented.

## License

This project is licensed under the MIT License.


## Reflection

This was one of my earliest Python projects and one of the first times I worked with a third-party library.

Learning how to use the `cryptography` package, generate an encryption key, and securely encrypt and decrypt passwords was both challenging and exciting. Looking back, I can see many ways to improve this project, but it represents an important milestone in my programming journey.