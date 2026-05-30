# 🛡️ Caesar Cipher Tool (Basic Encryption & Decryption)

A simple and efficient Python script designed to encrypt and decrypt text using the classic **Caesar Cipher** technique to secure data in transit.

This repository represents **Project 2** for the **DecodeLabs Cybersecurity Internship**.

---

## 🚀 Features

* **Encryption:** Converts raw plaintext into unreadable ciphertext by shifting characters forward by a fixed key.
* **Decryption:** Reverses the ciphertext back into its original readable form using the same key.
* **Data Integrity:** Fully preserves character casing (handles uppercase and lowercase separately) while keeping spaces, numbers, and special symbols intact.
* **IPO Model Alignment:** The code structure perfectly follows the (Input -> Process -> Output) architecture outlined in the lab guidelines.

---

## 📊 How It Works (Cryptographic Logic)

The tool processes the text character by character and applies basic modular arithmetic:
* **Encryption Formula:** `New Character = (Current Character Index + Shift Key) % 26`
* **Decryption Formula:** `Original Character = (Cipher Character Index - Shift Key) % 26`

---

## 🛠️ How to Run Locally

1. Ensure you have Python installed on your machine.
2. Run the script directly from your terminal or command prompt:
   ```bash
   python caesar_cipher.py