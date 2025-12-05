# 🔐 AES File Encryption & Decryption (Python)

 A simple & secure file encryption/decryption tool built using **AES-256 (CBC Mode)** & **PBKDF2** key derivation.
 
 This script allows you to protect any file using a password-based encryption system.

## 🚀 Features

 - AES-256 encryption (CBC mode)
 - Secure key derivation with PBKDF2 (100k iterations)
 - Random salt & IV for every encryption
 - Hidden password input using getpass()
 - Password strength checking [`zxcvbn`] 
 - Safe padding/unpadding
 - Handles incorrect passwords gracefully
 - Simple interactive CLI

## 📂 Project Structure

 ```perl
 📁 aes-cbc-encryption
 ├── aes_cipher.py
 └── README.md
 ```

## 📦 Requirements

 Install dependencies via pip:

 ```bash
 pip install pycryptodome zxcvbn
 ```

## 🧠 How it works

 - A random **16-bytes Salt** is generated
 - PBKDF2 derives a **32-byte key** from password 
 - AES CBC mode encrypts the file data
 - Output file format

 ```css
 [Salt][IV][Encrypted_Data]
 ```

 This format contains everything needed for secure decryption.

## 1️⃣ Clone the Repository

 ```bash
 git clone https://github.com/m-rishad78/aes-cbc-encryption.git
 ```

## 2️⃣ Navigate to the Project Directory

 ```bash
 cd aes-cbc-encryption
 ```

## ▶️ Usage

 Run the program

 ```bash
 python aes_cipher.py
 ```

 Then choose an option

 ```css
    1. Encryption
    2. Decryption
 ```

## 🔑 Encryption Example

 ```css
 Enter the Filename: secret.txt
 Enter the Password: ******
 
 File Has been Successfully Encrypted.
 ```
 
 This genrates:
     secret.txt.enc

## 🔓 Decryption Example

 ```css
 Enter the Filename: secret.txt.enc
 Enter the Password: ******
 
 File Has been Successfully Decrypted.
 ```
 
 Restores the original file:
   secret.txt

## ⚠️ Security Notes

 - Use strong passwords for better protection
 - never share **.enc** file & passwords together
 - This project is for learning & personal use - not for high-security production systems

## ⭐ Contribute

 Feel free to open issues or submit pull requests to improve the project!

## 📜 License

 This project is licensed under the **MIT License**.