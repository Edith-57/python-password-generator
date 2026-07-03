# 🔐 Python Password Generator

A simple yet secure command-line password generator built with Python.

This project generates strong random passwords while ensuring they meet basic security requirements. The user can customize the password length, choose whether to include special characters, and regenerate passwords until satisfied.

---

## ✨ Features

* 🔒 Enforces a minimum password length of **12 characters** for better security.
* 🔡 Guarantees at least **one lowercase letter**.
* 🔠 Guarantees at least **one uppercase letter**.
* 🔢 Guarantees at least **one numeric digit**.
* ✨ Optionally guarantees at least **one special character**.
* 🎲 Randomly shuffles all characters to improve password randomness.
* 🔄 Allows users to regenerate passwords until they are satisfied.
* 💻 Simple command-line interface with easy user interaction.

---

## 🛠️ Technologies Used

* Python 3
* Python `random` module

---

## 📂 Project Structure

```text
python-password-generator/
│
├── password_generator.py
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Edith-57/python-password-generator.git
```

2. Open the project folder.

3. Run the program:

```bash
python password_generator.py
```

---

## 📋 Example

```text
Enter the password length: 16
Include special characters? (yes/no): yes

vQ2$A7b!mN8xL@rP

Satisfied with this password? (yes/no): no

6^TkP1hQ9@LmY4wA

Satisfied with this password? (yes/no): yes

Thanks for using the password generator!
```

---

## ⚙️ How It Works

1. The user enters the desired password length.
2. If the entered length is less than 12, the program automatically sets it to 12.
3. The user chooses whether special characters should be included.
4. The program guarantees the required character types by selecting:

   * One lowercase letter
   * One uppercase letter
   * One digit
   * One special character (if enabled)
5. The remaining characters are selected randomly from the appropriate character pool.
6. The password characters are shuffled to ensure a random order.
7. The generated password is displayed.
8. If the user is not satisfied, a new password is generated until the user accepts one.

---

## 🔒 Security Rules

* Minimum password length of **12 characters**.
* Every generated password contains:

  * At least one lowercase letter
  * At least one uppercase letter
  * At least one number
* If special characters are enabled, the password also contains at least one special character.
* Characters are shuffled before the password is returned to avoid predictable patterns.

---

## 🚀 Future Improvements

* Password strength meter
* Copy password directly to clipboard
* Graphical User Interface (GUI)
* Save generated passwords securely
* Export passwords to a file
* Option to exclude ambiguous characters (such as `O`, `0`, `I`, and `l`)
* Support for custom character sets

---

## 👨‍💻 Author

**Edith-57**

Built as a Python learning project while practicing functions, loops, lists, randomization, and user interaction.

---

## 📜 License

This project is open-source and available under the MIT License.
