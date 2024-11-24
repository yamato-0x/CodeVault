# Code Vault 🏦🔒

**A simple, secure way to store sensitive information like API keys, passwords, and secrets.**

---

## Overview

Code Vault is a Python application that lets you store your secrets in an encrypted vault. You can easily add, retrieve, and protect your sensitive data using strong encryption techniques. Ideal for developers who want to keep their credentials safe!

---

## Features

- **Secure Storage**: All secrets are encrypted using AES-256 encryption, making them unreadable without the master key.
- **Simple Command-Line Interface**: Easy-to-use commands for adding and retrieving secrets.
- **Lightweight**: No complex setups. Just download, run, and you’re good to go.
- **Cross-Platform**: Works on any OS with Python installed (Windows, macOS, Linux).

---

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine. If not, download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yamato-0x/CodeVault.git
   cd code-vault

2. **Install dependencies:**
    - Install the required Python package:
   ```bash
   pip install cryptography

3. **Run the application:**
   ```bash
   python vault.py

---

## Usage
*Once you run the application, you'll be presented with a menu:*

>Welcome to Code Vault!
> 1. Add a secret
> 2. Get a secret
> 3. Exit

-  **Add a secret:** You’ll be prompted to enter a name and a value for your secret, which will be encrypted and saved in your vault.

-  **Get a secret:** Enter the name of a stored secret to retrieve its value. The app will decrypt it and show you the original value.

-  **Exit:** Quit the application.

---

## How It Works

1. **Encryption:**
  The app uses the `cryptography` library to encrypt and decrypt secrets. The master key (`key.key`) is stored securely, and only it can unlock your secrets.

2. **Storage:**
  Secrets are stored in a `vault.json` file in encrypted form. Each secret is indexed by its name.

3. **Master Key:**
  The `key.key` file contains the encryption key, and it is required for both encrypting and decrypting secrets. You only need to generate the key once.

---
### Contributing
We welcome contributions to improve the Code Vault!

- Fork the repo.
- Create a new branch.
- Make your changes.
- Submit a pull request.

---
### Contact
- Author: Yamato-0x
- Project Link: https://github.com/yamato-0x/CodeVault.git
- Social: [Discord](https://discord.gg/zutrhhYRyz) 
---
Made with 💻 by [Yamato-0x](https://github.com/yamato-0x)







